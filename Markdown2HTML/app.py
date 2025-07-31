import markdown
from pathlib import Path
import glob

def Translate(MDfile, template_file="./html/template.html"):
    # Lire Markdown
    with open(MDfile, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Convertir Markdown en HTML
    html_content = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

    # Charger template
    with open(template_file, "r", encoding="utf-8") as f:
        template = f.read()

    # Préparer le titre et le h1
    title = Path(MDfile).stem

    # Injecter dans template
    final_html = template.format(title=title, H1=title, content=html_content)

    # Écrire fichier html unique pour ce md
    output_path = Path("./html") / f"{title}.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"{MDfile} -> {output_path} généré.")


fichiersMD = glob.glob("./md/*.md")
fichiersHTML = glob.glob("./html/*.html")

# Extraire les noms de fichiers sans extension avec pathlib
nomsMD = [Path(fichier).stem for fichier in fichiersMD]
nomsHTML = [Path(fichier).stem for fichier in fichiersHTML]

fichiers = [nom for nom in nomsMD if nom not in nomsHTML]
print("Les fichiers suivants vont être traduit en HTML : ",fichiers)
for i in fichiers:
    Translate(f"./md/{i}.md")