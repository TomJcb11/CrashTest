# Documentation du Programme de Conversion Markdown vers HTML

## Introduction

Ce programme permet de convertir des fichiers Markdown (.md) en fichiers HTML. Il facilite la création de documents HTML à partir de Markdown, en intégrant des tableaux, des images, des liens, et d'autres éléments typiques du Markdown.

## Fonctionnalités

- Conversion de fichiers Markdown en HTML.
- Prise en charge des tableaux Markdown grâce à la bibliothèque markdown2.
- Génération automatique des fichiers HTML dans un répertoire spécifique.
- Gestion des fichiers existants pour éviter les doublons.
- Styles CSS intégrés pour un rendu esthétique des documents HTML.

## Prérequis

Avant d'exécuter le programme, assurez-vous d'avoir les éléments suivants :

- Python 3.x installé sur votre machine.
- Bibliothèque markdown2 installée. Vous pouvez l'installer via pip :

```bash
pip install markdown2
```

## Installation

Clonez le dépôt ou téléchargez le code source. Assurez-vous d'avoir la structure de fichiers suivante :

```css
.
├── Markdown2HTML.py
├── css
│   └── styles.css
├── md
│   ├── exemple.md
│   ├── 1.md
│   ├── 2.md
│   └── 3.md
└── html
```

## Utilisation

Placez vos fichiers Markdown (.md) dans le dossier md.

Exécutez le programme avec la commande suivante :

```bash
python Markdown2HTML.py
```

Les fichiers HTML générés seront sauvegardés dans le dossier html.

## Structure des Fichiers

* `Markdown2HTML.py` : Fichier principal qui effectue la conversion.
* `css/styles.css` : Fichier CSS qui définit le style des fichiers HTML générés.
* `md/` : Répertoire contenant les fichiers Markdown à convertir.
* `html/` : Répertoire où les fichiers HTML générés seront stockés.

## Fonctionnement du Code

### Importation des Bibliothèques

Le programme commence par importer les bibliothèques nécessaires :

```python
import os
import glob
from pathlib import Path
import markdown2
```

### Fonction de Traduction

La fonction `Translate(MDfile)` lit un fichier Markdown, le convertit en HTML et écrit le résultat dans un nouveau fichier HTML. Elle gère également les erreurs si le fichier Markdown n'existe pas.

### Lecture des Fichiers

Le programme lit tous les fichiers Markdown dans le répertoire md et vérifie ceux qui n'ont pas encore été convertis en HTML. Pour ce faire, il utilise la bibliothèque glob pour lister les fichiers Markdown et HTML.

### Conversion des Fichiers

Pour chaque fichier Markdown non converti, la fonction `Translate` est appelée, ce qui permet de créer les fichiers HTML dans le dossier html.

### Application du CSS

Un lien vers le fichier CSS est inclus dans chaque fichier HTML généré pour appliquer le style souhaité.

## Personnalisation

### Modification du CSS

Pour personnaliser l'apparence des fichiers HTML générés, modifiez le fichier `styles.css` en fonction de vos préférences.
