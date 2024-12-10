class Betail:
    def __init__(
        self, nom, duree_vie, nourriture_quotidienne, eau_necessaire, valeur, produit=""
    ):
        self.nom = nom
        self.en_vie = True
        self.duree_vie = duree_vie
        self.nourriture_quotidienne = nourriture_quotidienne
        self.eau_necessaire = eau_necessaire
        self.produit = produit
        self.produit_mort = "viande"
        self.valeur = valeur
        self.sante = "ok"

    def nourrir(self, nourriture_disponible, eau_disponible):
        if (
            nourriture_disponible >= self.nourriture_quotidienne
            and eau_disponible >= self.eau_necessaire
        ):
            print(f"{self.nom} a été nourri et abreuver aujourd'hui.")
        else:
            print(f"{self.nom} n'a pas reçu assez de nourriture ou d'eau aujourd'hui !")
            self.sante = "malade"
            self.en_vie = False

    def produire(self):
        if self.en_vie:
            print(f"{self.nom} produit : {self.produit}.")
            return self.produit
        else:
            print(f"{self.nom} est mort et ne peut plus produire.")
            return "viande"
