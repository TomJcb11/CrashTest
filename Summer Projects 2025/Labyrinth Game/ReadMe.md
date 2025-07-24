
# 🧩 Projet Labyrinthe — Révision POO Python

Ce projet est un **jeu de labyrinthe en Python** conçu pour réviser en profondeur le paradigme orienté objet. Il repose sur une architecture modulaire et évolutive, illustrant tous les grands principes de la programmation orientée objet.

---

## 🗺️ Objectifs pédagogiques

- Revoir et mettre en pratique les **concepts fondamentaux de la POO** :
  - Encapsulation
  - Héritage
  - Polymorphisme
  - Abstraction
  - Composition
- Structurer un projet Python en modules clairs
- Gérer un moteur de jeu simple avec interactions
- Implémenter un labyrinthe procédural avec IA de poursuite
- (Bonus) Ajouter une GUI interactive (Turtle ou autre)

---

## 🧱 Structure du projet

```
labyrinthe/
├── main.py
├── moteur_jeu.py
├── models/
│   ├── Grids/
│   │   └── grille_base.py
│   ├── Players/
│   │   ├── joueur.py
│   │   ├── monstre.py
│   └── moteur.py
├── utils/
│   ├── pathfinding.py
│   └── constantes.py
├── cartes/
│   └── ...
└── README.md
```

---

## 📅 Roadmap d’apprentissage (10 jours)

### 🟩 Jour 1 – Rappel des bases OOP + Initialisation
- Classes, objets, attributs, méthodes
- Créer les premières classes : `Grid`, `Joueur`, `Monstre`
- Objectif : structure minimale qui tourne

### 🟩 Jour 2 – Héritage & modularité
- Créer une base de grille et des variantes (héritage)
- Préparer les extensions futures

### 🟩 Jour 3 – Encapsulation & composition
- Protéger les données internes
- Une grille **contient** un joueur, un monstre, etc.

### 🟩 Jour 4 – Polymorphisme
- Unifier les comportements (`deplacer()`, `afficher()`)
- Classe abstraite `Personnage` (optionnelle)

### 🟩 Jour 5 – Génération procédurale
- Créer un labyrinthe avec un algorithme (DFS, Prim)
- Associer entrée/sortie au hasard

### 🟩 Jour 6 – Pathfinding et logique IA
- BFS ou A* pour que le monstre poursuive le joueur
- Module `pathfinding.py` indépendant

### 🟩 Jour 7 – Moteur de jeu
- Orchestrer grille, joueur, monstre dans `MoteurJeu`
- Détection de victoire ou défaite

### 🟩 Jour 8 – Entrées clavier abstraites
- Créer un système d’input
- Préparer la transition vers une GUI (ex : Turtle)

### 🟩 Jour 9 – Tests unitaires & refacto
- Ajouter des tests avec `pytest`
- Corriger, documenter, nettoyer

### 🟩 Jour 10 – Synthèse & bonus
- Export de cartes (SVG, CSV…)
- Transition vers interface graphique (Turtle, Pygame…)

---

## 🧠 Concepts OOP mis en pratique

| Concept       | Appliqué dans…                     |
|---------------|------------------------------------|
| Encapsulation | Attributs protégés (`_position`)   |
| Héritage      | `Joueur`, `Monstre` ⟵ `Personnage` |
| Polymorphisme | Méthodes communes sur différents objets |
| Abstraction   | `InputHandler`, `GrilleBase`       |
| Composition   | `MoteurJeu` contient tous les objets |
| Couplage faible | Fichiers / modules bien séparés |

---

## 🚀 Bonus possibles

- Interface Turtle ou Pygame
- Menu de démarrage
- Sauvegarde de cartes
- Editeur de niveaux
- Sons / Musique

---

## 🧪 Dépendances

- Python 3.10+
- (optionnel) `pytest` pour les tests
- (optionnel) `pygame` ou `turtle` pour l’interface

---

## 📌 Lancement

```bash
python main.py
```

---

## 📂 À venir

- README interactif avec GIF du gameplay
- Export / import de cartes personnalisées
- Jouabilité clavier ou clic

---

## 🧑‍💻 Auteur

Ce projet est développé dans un but pédagogique de révision OOP.  
Parfait pour progresser en Python tout en s’amusant.
