import os
import time

from models.instances.store import marche_items
from models.ferme import Ferme


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def afficher_marche():
    clear_console()
    print("--- Produits Disponibles au Marché ---")
    # time.sleep(2)
    for idx, item in enumerate(marche_items):
        print(
            f"{idx + 1}. {item.name} - {item.value} crédits - Conservation : {item.conservation}"
        )


def acheter_produit(ferme, produit_index, quantite):
    produit = marche_items[produit_index]
    cout_total = produit.value * quantite

    if ferme.solde_credit >= cout_total:
        ferme.solde_credit -= cout_total
        print(
            f"Acheté {quantite} {produit.name} pour {cout_total} crédits., il vous reste {ferme.solde_credit} crédits"
        )
        ferme.ajouter_a_l_inventaire(produit, quantite)
        print(ferme.invetory)
    else:
        print(
            f"Pas assez de crédits pour acheter {quantite} {produit.name}. Solde actuel : {ferme.solde_credit}"
        )


# Exemple d'utilisation dans le programme principal
def main():
    ferme = Ferme("La belle prairie")
    message_bienvenue = """
    Bienvenue à la ferme! Vous avez 500 crédits pour commencer.
    Vous pouvez acheter des produits au marché pour les revendre plus tard.
    Vous allez devoir cultiver et récolter vos propres produits mais aussi élever vos bètes dans votre ferme.
    chaque jours vous aurez des tâches à accomplir pour faire prospérer votre ferme.
    """
    Message_jour = f""" Jour n° {ferme.nombre_jours}
    Quel est le programme du jour?
        -1 :Marché (acheter et revendre des produits)
        -2 :Inventaire (consultez vos stock et betes)
        -3 :Ferme (cultiver, récolter, élever) vous pourrer aussi améliorer votre ferme ici.
        -4 :Jour suivant (passer au jour suivant les frais de fonctionnement de la ferme seront déduits et un jour de durabilité sera retiré à vos produits)
        -5 :Sauvegarder et quitter
    """
    message_ferme = """
    Vous voici dans la ferme que voulez vous faire?
     -c : acheter un nouvel emplacment de culture
     -e : acheter un nouvel enclos
     -q : quitter
    
    """

    if ferme.nombre_jours < 1:
        print(message_bienvenue)
        input("Appuyez sur entrée pour continuer...")
    clear_console()
    choix = input(Message_jour)

    match choix:
        case "1":
            afficher_marche()
            produit_index = (
                int(input("Choisissez un produit à acheter (numéro) : ")) - 1
            )
            quantite = int(input("Entrez la quantité : "))
            acheter_produit(ferme, produit_index, quantite)
        case "3":
            print(
                "Vous avez choisi la ferme, ici vous améliorer votre ferme, acheter des cultures ou des enclos \n"
            )
            ferme.afficher_etat()
            action = input(message_ferme)
            match action:
                case "c":
                    print(ferme.ameliorer_culture())

                case "e":
                    print(ferme.ameliorer_enclos())
                case "q":
                    pass
                case _:
                    print("Action non reconnue")
            print(action)

    # time.sleep(1.52)
    clear_console()


main()
