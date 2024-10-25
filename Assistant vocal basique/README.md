# Assistant vocal basique

## Description

Le but est de créer un assistant vocal capable de comprendre des commandes vocales et de répondre en parlant. L'assistant pourrait effectuer des tâches simples comme donner la météo, effectuer des calculs, ou ouvrir des applications.

## Fonctionnalités

- **Reconnaissance vocale** pour capturer et interpréter les commandes de l'utilisateur.
- **Synthèse vocale** pour répondre aux commandes (utilisation de `pyttsx3`).
- Fonctionnalités principales :\* **Météo**: Récupérer et annoncer la météo actuelle via une API.
  - **Calculs**: Répondre à des questions mathématiques simples.
  - **Gestion de fichiers**: Ouvrir des fichiers ou applications sur demande.

## Outils/Bibliothèques utiles

- **SpeechRecognition** pour la reconnaissance vocale.
- **pyttsx3** pour la synthèse vocale (voix de l'assistant).
- **API météo** pour les informations météorologiques (ex : OpenWeather).
- **Module OS** pour exécuter des commandes systèmes.

## Challenges

- Gérer les erreurs de reconnaissance vocale et les requêtes ambiguës.
- Optimiser la réactivité de l'assistant.
- Créer une structure modulaire pour gérer plusieurs types de commandes.

## Extensions possibles

- Ajouter des fonctionnalités personnalisées ou l'intégration de nouveaux services (commandes domotiques, contrôle des appareils).
- Créer une interface graphique pour l’assistant, permettant une interaction plus visuelle.
