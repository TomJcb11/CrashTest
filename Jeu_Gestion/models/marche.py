class Marche:
    def __init__(self, name, value, conservation, offer, demand):
        self.offre = 50
        self.demande = 50
        self.conservation = (
            "Illimité" if conservation is None else f"{conservation} jours"
        )
        self.name = name
        self.value = value
        self.offer = offer
        self.demand = demand

    def calculer_prix(self, valeur_unitaire):
        facteur_demande = 1 + (self.demande - 50) / 100
        facteur_offre = 1 - (self.offre - 50) / 100
        return round(valeur_unitaire * facteur_demande * facteur_offre, 2)

    def mettre_a_jour(self, variation_offre, variation_demande):
        self.offre = max(1, min(100, self.offre + variation_offre))
        self.demande = max(1, min(100, self.demande + variation_demande))
