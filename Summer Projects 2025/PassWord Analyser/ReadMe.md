# 🔐 Projet – Password Auditor & Strength Analyzer

## 🎯 Objectif

Ce projet permet d’auditer une base de données de mots de passe (CSV, JSON ou TXT) afin d’identifier :

- Les faiblesses (longueur, complexité…)
- Les duplications
- La fréquence de patterns connus (ex. `1234`, `qwerty`, `azerty`, etc.)
- Une estimation de leur robustesse face à un brute-force

Bonus :
- Génération de mots de passe forts
- Export d’un rapport (txt ou HTML)
- Intégration d’un dictionnaire de mots à éviter

---

## 📦 Structure du projet (exemple)
```css
password_auditor/
├── data/
│ └── passwords.csv
├── src/
│ ├── init.py
│ ├── main.py
│ ├── loader.py
│ ├── analyzer.py
│ └── generator.py
├── output/
│ └── report.txt / report.html
└── requirements.txt
```
## 🧩 Analyse des faiblesses possibles

Tu peux détecter les faiblesses suivantes (via conditions ou regex) :

- Mot de passe trop court (< 8 caractères)
- Uniquement minuscules / majuscules
- Contient uniquement des chiffres
- Suite évidente : `1234`, `abcd`, `qwerty`, etc.
- Mots trouvés dans un dictionnaire connu
- Contient une année (`19xx` ou `20xx`)
- Mot de passe dupliqué

### 📌 Regex utiles :

```python
r'(.)\1{2,}'         # caractères répétés
r'(1234|abcd|qwerty)'# séquences courantes
r'^[a-z]+$'          # uniquement minuscules
r'\d{4}'             # années
```

## 🧠 Design orienté objet (exemple simple)

```python
class Password:
    def __init__(self, raw: str):
        self.raw = raw
        self.weaknesses = []
        self.entropy = 0

    def analyze(self):
        # analyse individuelle du mot de passe
        pass

class PasswordAnalyzer:
    def __init__(self, password_list: list[str]):
        self.passwords = [Password(p) for p in password_list]

    def run(self):
        for pwd in self.passwords:
            pwd.analyze()

    def report(self):
        # export des résultats
        pass
```

## 🔢 Estimation d’entropie
Formule simple :

```python
entropy = log2(possible_chars ** len(password))
```
Avec :

- 26 lettres min
- 26 lettres maj
- 10 chiffres
- ~30+ symboles

Plus il y a de diversité dans les types de caractères, plus l’entropie est élevée.

## 📊 Rapport final
Contenu du rapport (en .txt ou .html) :

- Top 10 mots de passe les plus fréquents
- Pourcentage de mots faibles
- Mot de passe dupliqués
- Suggestions de mots de passe forts

## 🎁 Générateur de mots de passe robustes
```python
import random, string

def generate_strong_password(length=12):
    pool = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(pool) for _ in range(length))
```
## 📂 Données d'exemple (passwords.csv)

```csv
id,password
1,123456
2,password
3,hello123
4,qwerty
5,s3cur3Pa$$
6,admin
7,welcome
8,azerty
```

