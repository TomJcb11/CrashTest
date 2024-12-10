from models import marche

marche_items = [
    marche.Marche(
        name="oeuf de poules", value=1, conservation=14, offer=10, demand=0.5
    ),
    marche.Marche(name="oeuf de canard", value=2, conservation=8, offer=8, demand=1.0),
    marche.Marche(
        name="oeuf de poules fécondé", value=2, conservation=7, offer=7, demand=1.5
    ),
    marche.Marche(
        name="oeuf de canard fécondé", value=3, conservation=4, offer=5, demand=2.0
    ),
    marche.Marche(
        name="Laine de mouton", value=5, conservation=20, offer=15, demand=3.0
    ),
    marche.Marche(name="Lait", value=10, conservation=30, offer=20, demand=5.0),
    marche.Marche(name="Veau", value=10, conservation=30, offer=10, demand=8.0),
    marche.Marche(name="Porcelet", value=8, conservation=25, offer=12, demand=6.0),
    marche.Marche(name="Agneau", value=5, conservation=20, offer=10, demand=4.0),
    marche.Marche(name="Blé", value=1, conservation=30, offer=50, demand=0.2),
    marche.Marche(name="Maïs", value=3, conservation=30, offer=30, demand=1.0),
    marche.Marche(name="Carottes", value=2, conservation=30, offer=25, demand=0.8),
    marche.Marche(name="Riz", value=6, conservation=30, offer=20, demand=3.0),
    marche.Marche(
        name="Pommes de terre", value=3, conservation=30, offer=30, demand=1.0
    ),
    marche.Marche(name="Tomates", value=4, conservation=30, offer=20, demand=2.0),
    marche.Marche(name="Laitue", value=3, conservation=30, offer=25, demand=1.5),
    marche.Marche(name="Aubergines", value=6, conservation=30, offer=15, demand=3.0),
    marche.Marche(name="Fraises", value=5, conservation=30, offer=20, demand=2.5),
    marche.Marche(name="Oignons", value=2, conservation=30, offer=30, demand=1.0),
    marche.Marche(name="Eau (50L)", value=12, conservation=None, offer=10, demand=6.0),
]
