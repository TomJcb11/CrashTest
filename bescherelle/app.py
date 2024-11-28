import streamlit as st
import pandas as pd

csv_file = "./DB/verbList.csv"

# Dictionnaires de correspondance pour les modes et les temps
mode_dict = {
    "inf": "infinitif",
    "ind": "indicatif",
    "sub": "subjonctif",
    "par": "participe",
    "imp": "impératif",
    "cnd": "conditionnel",
}

tense_dict = {
    "pre": "présent",
    "imp": "imparfait",
    "pas": "passé",
    "fut": "futur",
}


# Lire le fichier csv avec le bon séparateur
verbs = pd.read_csv(csv_file, sep=";")

# Créer un DataFrame à partir des données lues
df = pd.DataFrame(verbs)


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

    # Créer un dictionnaire de DataFrames pour chaque mode/temps
    dataframes = {}
    for mode, tenses in conjugation_dict.items():
        for tense, conjugations in tenses.items():
            sorted_conjugations = sort_conjugations(conjugations)
            data = {"Conjugation": sorted_conjugations}
            df_mode_tense = pd.DataFrame(data)
            dataframes[f"{mode} - {tense}"] = df_mode_tense

    return dataframes


# récupérer tous les verbes uniques
def retrieve_all_verbs():
    return df["lemme"].unique()


all_verbs = retrieve_all_verbs()

# Création de la page Streamlit
st.header("Streamlit Bescherelle")

chosen_verb = st.selectbox(
    label="Choisissez le verbe dont vous souhaitez la conjugaison", options=all_verbs
)

if chosen_verb:
    filtered_df = get_verbs_by_lemme(df, chosen_verb)
    conjugation_dfs = display_conjugation(filtered_df)

    st.subheader(f"Lemme: {chosen_verb}")
    for key, df_mode_tense in conjugation_dfs.items():
        st.subheader(key)
        st.dataframe(df_mode_tense)
