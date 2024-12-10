from models.culture import Culture
from models.betail import Betail
from models.marche import Marche


class Ferme:
    def __init__(self, nom):
        self.nom = nom
        self.production_list = []
        self.invetory = []
        self.nombre_culture = 2
        self.nombre_enclos = 0
        self.solde_credit = 500
        self.nombre_jours = 0
        self.reserve_eau = 100

    def ajouter_a_l_inventaire(self, marche, quantity):
        self.invetory.append({
            "produit": marche.name,
            "quantite": quantity,
            "valeur": marche.value,
            "conservation": marche.conservation,
        })

    def ajouter_culture(self, culture):
        self.production_list.append(culture)
        self.nombre_culture += 1
        self.solde_credit -= culture.cout

    def ajouter_betail(self, betail):
        self.production_list.append(betail)
        self.nombre_enclos += 1
        self.solde_credit -= betail.valeur

    def ameliorer_culture(self):
        if self.nombre_culture >= 10 and self.solde_credit >= 1000:
            self.nombre_culture += 1
            self.solde_credit -= 1000
            return f"Vous avez acheté une {self.nombre_culture}ème culture pour 1000 crédits."
        elif self.nombre_culture >= 5 and self.solde_credit >= 600:
            self.nombre_culture += 1
            self.solde_credit -= 600
            return f"Vous avez acheté une {self.nombre_culture}ème culture pour 600 crédits."
        elif self.nombre_culture >= 3 and self.solde_credit >= 300:
            self.nombre_culture += 1
            self.solde_credit -= 300
            return f"Vous avez acheté une {self.nombre_culture}ème culture pour 300 crédits."
        else:
            if self.solde_credit >= 200:
                self.nombre_culture += 1
                self.solde_credit -= 200
                return f"Vous avez acheté une {self.nombre_culture}ème culture pour 200 crédits."
            else:
                return "Vous n'avez pas assez de crédits pour améliorer votre culture."

    def ameliorer_enclos(self):
        if self.nombre_enclos >= 10 and self.solde_credit >= 5000:
            self.nombre_enclos += 1
            self.solde_credit -= 5000
            return (
                f"Vous avez acheté un {self.nombre_enclos}ème enclos pour 5000 crédits."
            )
        elif self.nombre_enclos >= 5 and self.solde_credit >= 2000:
            self.nombre_enclos += 1
            self.solde_credit -= 2000
            return (
                f"Vous avez acheté un {self.nombre_enclos}ème enclos pour 2000 crédits."
            )
        elif self.nombre_enclos >= 3 and self.solde_credit >= 1000:
            self.nombre_enclos += 1
            self.solde_credit -= 1000
            return (
                f"Vous avez acheté un {self.nombre_enclos}ème enclos pour 1000 crédits."
            )
        else:
            if self.solde_credit >= 500:
                self.nombre_enclos += 1
                self.solde_credit -= 500
                return f"Vous avez acheté un {self.nombre_enclos}ème enclos pour 500 crédits."
            else:
                return "Vous n'avez pas assez de crédits pour améliorer votre enclos."

    def afficher_etat(self):
        print(f"{self.nom}")
        print(f"Crédits: {self.solde_credit}")
        print(f"Emplacement de cultures: {self.nombre_culture}")
        print(f"Nombre d'enclos: {self.nombre_enclos}")
        print(f"Réserve d'eau: {self.reserve_eau}")

    def passer_jour(self):
        self.nombre_jours += 1
        for item in self.production_list:
            if isinstance(item, Culture):
                item.arroser(self.reserve_eau)
                self.reserve_eau -= item.eau_necessaire
            elif isinstance(item, Betail):
                item.nourrir(2, item.eau_necessaire)
                self.reserve_eau -= item.eau_necessaire

        # Vérifier les conditions de fin de jeu
        if self.solde_credit < 1:
            print("Game Over : Vous n'avez plus de crédits.")
            exit()

    def vendre_production(self, marche):
        total_vente = 0
        for item in self.production_list:
            if isinstance(item, Culture) and item.etat == "prêt à récolter":
                total_vente += marche.calculer_prix(item.rendement)
                self.production_list.remove(item)
                self.nombre_culture -= 1
            elif isinstance(item, Betail) and item.en_vie:
                produit = item.produire()
                total_vente += marche.calculer_prix(item.valeur)
        self.solde_credit += total_vente
        print(f"Vous avez vendu votre production pour {total_vente} crédits.")
