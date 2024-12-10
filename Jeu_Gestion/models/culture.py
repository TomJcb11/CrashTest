class Culture:
    def __init__(self, nom, duree, cout, rendement, eau_necessaire):
        self.nom = nom
        self.duree = duree
        self.cout = cout
        self.rendement = rendement
        self.eau_necessaire = eau_necessaire
        self.etat = "graines"
        self.croissance = 0

    def arroser(self, eau_disponible):
        if eau_disponible >= self.eau_necessaire:
            self.croissance += 100 / self.duree
            print(
                f"{self.nom} a été arrosé. Croissance actuelle : {self.croissance:.2f}%"
            )
        else:
            print(f"Pas assez d'eau pour arroser {self.nom}.")
        if self.croissance >= 100:
            self.etat = "prêt à récolter"

    def recolter(self):
        if self.etat == "prêt à récolter":
            print(f"Récolte de {self.rendement} unités de {self.nom}.")
            self.croissance = 0
            self.etat = "graines"
            return self.rendement
        else:
            print(f"{self.nom} n'est pas encore prêt à être récolté.")
            return 0
