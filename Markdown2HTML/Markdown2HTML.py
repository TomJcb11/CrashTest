import os
import glob
from pathlib import Path
import markdown2

def Translate(MDfile):
    """
    Translate a markdown file to HTML file.
    
    :param MDfile: the markdown file to translate
    :type MDfile: str
    :raises FileNotFoundError: if the markdown file does not exist
    :raises Exception: for any errors during the conversion process
    """
    # Vérifier si le fichier existe
    if not os.path.isfile(MDfile):
        raise FileNotFoundError(f"Le fichier {MDfile} n'existe pas.")
    
    # Lire le contenu du fichier Markdown
    with open(MDfile, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Convertir le Markdown en HTML
   # Convertir le Markdown en HTML avec markdown2
    html_content = markdown2.markdown(md_content, extras=["tables"])

    # Créer le nom du fichier HTML
    html_file = f"./html/{Path(MDfile).stem}.html"

   # Ajouter la déclaration de style CSS
    html_output = f"""<!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{Path(html_file).stem}</title>
            <link rel="stylesheet" href="../css/styles.css">
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
# Écrire le contenu HTML dans un nouveau fichier
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_output)
    
    print(f"Le fichier {MDfile} a été traduit en {html_file}.")
    

fichiersMD = glob.glob("./md/*.md")
fichiersHTML = glob.glob("./html/*.html")

# Extraire les noms de fichiers sans extension avec pathlib
nomsMD = [Path(fichier).stem for fichier in fichiersMD]
nomsHTML = [Path(fichier).stem for fichier in fichiersHTML]

fichiers = [nom for nom in nomsMD if nom not in nomsHTML]
print("Les fichiers suivants vont être traduit en HTML : ",fichiers)
for i in fichiers:
    Translate(f"./md/{i}.md")
