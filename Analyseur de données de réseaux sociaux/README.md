# Analyseur de données de réseaux sociaux

## Description

Ce projet consiste à créer un analyseur qui récupère des données de réseaux sociaux (Twitter, Reddit, etc.) via des API, puis les analyse pour extraire des informations utiles comme la popularité des hashtags, la fréquence des mots-clés ou le sentiment global des utilisateurs.

## Fonctionnalités

- **Récupération de données** via API en fonction de mots-clés, hashtags ou utilisateurs.
- **Analyse des données**:\* Statistiques sur les hashtags les plus populaires.
  - Analyse de la fréquence des mots-clés.
  - Analyse de sentiments pour déterminer si les messages sont positifs, négatifs ou neutres.
- **Visualisation des résultats** à l’aide de graphiques (barres, nuages de mots, etc.).

## Outils/Bibliothèques utiles

- **Tweepy** pour l'API Twitter, **PRAW** pour Reddit.
- **Pandas** pour la manipulation des données.
- **Matplotlib / Seaborn** pour la visualisation des données.
- **TextBlob / VADER** pour l'analyse de sentiments.

## Challenges

- Gérer l'authentification API et les quotas de requêtes.
- Nettoyer et prétraiter les données récupérées.
- Optimiser l’analyse pour traiter efficacement de grandes quantités de données.

## Extensions possibles

- Créer un tableau de bord interactif en utilisant Flask ou Dash pour afficher les données en temps réel.
- Ajouter une analyse prédictive pour identifier des tendances futures.
