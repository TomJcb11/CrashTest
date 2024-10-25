# Générateur de texte Markdown en HTML

## Description

Ce projet consiste à créer un programme capable de convertir un fichier écrit en Markdown en un fichier HTML. Le programme devra reconnaître les différentes balises Markdown et les transformer en balises HTML correspondantes.

## Fonctionnalités

* Conversion des titres (`#`, `##`, etc.) en balises `<h1>`, `<h2>`, etc.
* Conversion du texte en gras, italique, et autres styles :* `**Gras**` → `<strong>Gras</strong>`
  * `*Italique*` → `<em>Italique</em>`
* Gestion des listes (à puces et numérotées).
* Support des liens et images :* `[Lien](http://exemple.com)` → `<a href="http://exemple.com">Lien</a>`
  * `![Image](image_url)` → `<img src="image_url" alt="Image">`
* Conversion des blocs de code Markdown en balises HTML `<pre><code>`.

## Outils/Bibliothèques utiles

* Utilisation de **regex** pour traiter les balises Markdown.
* Manipulation de fichiers avec Python (lecture et écriture).
* Option avancée : Utiliser des bibliothèques comme `markdown2` ou `mistune`.

## Challenges

* Gérer les cas particuliers (ex : balises imbriquées).
* Maintenir un bon équilibre entre la simplicité et la précision de la conversion.

## Extensions possibles

* Création d’une interface graphique (GUI) pour sélectionner des fichiers `.md` et générer le fichier `.html`.
* Ajouter un thème CSS automatique au fichier HTML pour améliorer le style visuel.
