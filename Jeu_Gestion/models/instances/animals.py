from models.betail import Betail

# Liste d'instances de bétail
liste_betails = [
    Betail(
        "Poule",
        duree_vie=7,
        nourriture_quotidienne=1,
        eau_necessaire=0.3,
        valeur=2,
        produit="oeuf de poules",
    ),
    Betail(
        "Vache",
        duree_vie=30,
        nourriture_quotidienne=3,
        eau_necessaire=1.5,
        valeur=10,
        produit="lait de vache",
    ),
    Betail(
        "Mouton",
        duree_vie=20,
        nourriture_quotidienne=2,
        eau_necessaire=0.8,
        valeur=5,
        produit="laine",
    ),
    Betail(
        "Cochon",
        duree_vie=25,
        nourriture_quotidienne=3,
        eau_necessaire=1.2,
        valeur=8,
    ),
    Betail(
        "Canard",
        duree_vie=10,
        nourriture_quotidienne=1,
        eau_necessaire=0.4,
        valeur=3,
        produit="oeuf de canard",
    ),
]
