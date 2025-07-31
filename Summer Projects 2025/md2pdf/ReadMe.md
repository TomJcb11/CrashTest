
# 📄 Markdown to PDF Converter (Proof of Concept)

## 🧠 Objectif

Un petit outil permettant de convertir un fichier Markdown (`.md`) en un fichier PDF stylisé via une étape HTML intermédiaire. Il vise à donner un rendu propre et personnalisable à tes notes Markdown, notamment pour une utilisation avec Obsidian, Zettelkasten ou tout autre outil de prise de notes.

---

## 🚀 Fonctionnalités

- Conversion `.md` ➝ `.html` ➝ `.pdf`
- Style CSS intégré (polices, titres, code, tableaux…)
- Prise en charge :
  - Blocs de code (```python)
  - Tableaux Markdown
- Compatible avec `markdown2` + `weasyprint`
- Facilement personnalisable avec du CSS

---

## 🧰 Prérequis

- Python 3.8+
- Modules Python :
  - `markdown2`
  - `weasyprint`

Installe-les avec pip :

```bash
pip install markdown2 weasyprint
```

---

## 📁 Structure du projet

```
.
├── md_to_pdf.py         # Fichier principal
├── note_exemple.md      # Exemple de markdown à convertir
├── note_exemple.pdf     # Résultat attendu
└── README.md
```

---

## 🧪 Exemple d'utilisation

```python
from md_to_pdf import md_to_pdf

md_to_pdf("note_exemple.md", "note_exemple.pdf")
```

---

## ⚙️ Fonctionnement

1. Lit le fichier `.md`
2. Le convertit en HTML avec `markdown2`
3. Y ajoute une couche CSS personnalisée
4. Utilise `weasyprint` pour générer un fichier PDF stylisé

---

## 🎨 Style intégré

Un CSS simple est injecté directement dans le HTML, gérant :
- Les titres (`h1`, `h2`, etc.)
- Les blocs de code (`<pre><code>`)
- Les tableaux
- Une lisibilité optimale avec une police sans-serif

Tu peux modifier ce style dans le fichier Python pour adapter l’apparence.

---

## 📌 Limitations

- Les images locales ne sont pas encore gérées (à venir)
- Pas encore de CLI complète
- Ne supporte pas les footnotes ou certains extras markdown complexes

---

## 🧱 Idées pour la suite

- Générer un PDF à partir de plusieurs fichiers `.md` (fusion)
- Ajout d’un template HTML via Jinja2
- Support des images locales
- Ligne de commande : `python md2pdf.py fichier.md --output fichier.pdf`
- Générer un sommaire ou index
- Choix de thème clair/sombre

---

## 📜 Licence

Projet personnel, libre de réutilisation et d’adaptation.
