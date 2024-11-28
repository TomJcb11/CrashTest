import pandas as pd
from APIkey import MONGODB_URI
from pymongo import MongoClient

csv_file = "./DB/verbList.csv"

# Dictionnaires de correspondance pour les modes et les temps
mode_dict = {
    "inf": "infinitif",
    "ind": "indicatif",
    "sub": "subjonctif",
    "par": "participe",
    "imp": "impératif",
}

tense_dict = {
    "pre": "présent",
    "imp": "imparfait",
    "pas": "passé",
    "fut": "futur",
}


def connect_to_db():
    client = MongoClient(MONGODB_URI)
    db = client.get_database()
    return db


# Fonction pour obtenir les verbes par lemme
def get_verbs_by_lemme(df, lemme):
    return df[df["lemme"] == lemme]


# Fonction pour trier les conjugaisons
def sort_conjugations(conjugations):
    order = {"1s": 0, "2s": 1, "3s": 2, "1p": 3, "2p": 4, "3p": 5}
    return sorted(conjugations, key=lambda x: order.get(x.split()[-1].strip("()"), 6))


# Fonction pour afficher la conjugaison en fonction de la grammaire infover
def display_conjugation(filtered_df):
    conjugation_dict = {}
    for index, row in filtered_df.iterrows():
        infover = row["infover"].split(";")
        for info in infover:
            if info and len(info.split(":")) == 3:
                mode, tense, person = info.split(":")
                mode_full = mode_dict.get(mode, mode)
                tense_full = tense_dict.get(tense, tense)
                conjugation = f"{row['Word']} ({person})"
                if mode_full not in conjugation_dict:
                    conjugation_dict[mode_full] = {}
                if tense_full not in conjugation_dict[mode_full]:
                    conjugation_dict[mode_full][tense_full] = []
                conjugation_dict[mode_full][tense_full].append(conjugation)

    for mode, tenses in conjugation_dict.items():
        print(f"{mode}:")
        for tense, conjugations in tenses.items():
            print(f"  {tense}:")
            sorted_conjugations = sort_conjugations(conjugations)
            for conjugation in sorted_conjugations:
                print(f"    {conjugation}")


# Fonction principale
def main():
    # Se connecter à MongoDB
    db = connect_to_db()
    print("Connected to MongoDB")

    # Collection pour stocker les réponses de l'API
    collection = db.verbList

    # Lire le fichier csv avec le bon séparateur
    verbs = pd.read_csv(csv_file, sep=";")

    # Créer un DataFrame à partir des données lues
    df = pd.DataFrame(verbs)

    # Exemple d'utilisation de la fonction get_verbs_by_lemme
    lemme = "avoir"
    filtered_df = get_verbs_by_lemme(df, lemme)

    # Afficher la conjugaison en fonction de la grammaire infover
    display_conjugation(filtered_df)


if __name__ == "__main__":
    main()
