
---

# Géographie de Kateb

## Description

**Géographie de Kateb** est un jeu interactif éducatif visant à aider les joueurs à améliorer leurs connaissances en géographie. Le jeu met au défi les joueurs d'identifier des pays à partir de leurs drapeaux, puis de deviner leurs capitales. Une nouvelle fonctionnalité permet également de sélectionner un continent spécifique pour personnaliser l'expérience de jeu.

Ce projet est développé en Python en utilisant le framework [BeeWare](https://beeware.org/) pour déployer l'application sur Android. Il exploite également la bibliothèque [Toga](https://toga.readthedocs.io/en/latest/) pour l'interface graphique et des ressources multimédias pour enrichir l'expérience de jeu.

## L’origine du projet

Tout a commencé avec une idée simple : créer un jeu éducatif immersif pour enseigner la géographie tout en s’amusant. Inspiré par l’amour des découvertes de Kateb, ce projet vise à rendre l’apprentissage des pays, de leurs capitales et de leurs drapeaux à la fois interactif et divertissant.

Avec cet objectif en tête, nous avons conçu un jeu stimulant qui combine cartes interactives, questions réflexives et exploration culturelle.

## Le passage de Python à Android

Pour transformer cette vision en une application mobile fonctionnelle, nous avons utilisé BeeWare, un framework Python puissant permettant de déployer facilement des applications multiplateformes, notamment sur Android. Bien que le chemin vers Android ait impliqué des défis techniques, chaque étape a été une leçon précieuse.

Le projet final est une application fluide et intuitive qui invite les utilisateurs à apprendre tout en jouant.

## Les étapes du développement

- **Idéation** : Concevoir un jeu basé sur la géographie et répondant à un besoin éducatif.
- **Prototypage Python** : Construire un modèle fonctionnel sur ordinateur.
- **Portage sur Android avec BeeWare** : Utiliser Briefcase pour générer l’APK.
- **Tests intensifs** : Régler les bugs et améliorer l’interface.
- **Ajout de la sélection des continents** : Permettre aux joueurs de choisir un continent ou de jouer sur le monde entier.
- **Intégration du classement en ligne** : Utilisation d'une API PHP pour enregistrer et afficher les scores des joueurs.

## Fonctionnalités principales

- **Apprentissage par les drapeaux et les cartes** : Identifiez les pays à partir de leurs drapeaux et explorez leurs cartes.
- **Sélection des continents** : Choisissez un continent spécifique (Afrique, Amérique, Asie, Europe, Océanie, Antarctique) ou jouez sur le monde entier.
- **Informations complètes** : Obtenez des détails sur la superficie, la population, la monnaie et plus encore.
- **Scores interactifs** : Suivez vos résultats et progressez à chaque partie.
- **Classement en ligne** : Comparez vos scores avec ceux des autres joueurs via une API PHP hébergée sur `http://studiokatebetpapa.mooo.com`.

## Installation

### Prérequis

Avant d'exécuter le jeu, assurez-vous d'avoir :

- **Python 3.8+** installé sur votre machine
- Les bibliothèques suivantes installées :
  ```sh
  pip install briefcase toga
  ```

### Clôner le projet

Vous pouvez également retrouver le code source sur GitHub : [GitHub - Géographie de Kateb](https://github.com/kattouba/GeographieKateb)

```sh
git clone https://github.com/kattouba/GeographieKateb
cd GeographieKateb
```

## Exécution du jeu

Pour générer et exécuter l'application sur Android :

```sh
briefcase create android
briefcase build android -u -r
```

## Structure du projet

```
GeographieKateb/
├── app.py  # Code principal du jeu
├── resources/
│   ├── flags/              # Images des drapeaux des pays
│   ├── maps/               # Cartes géographiques des pays
│   ├── info_restcountries/ # Informations sur chaque pays
│   ├── correct.mp3         # Son pour une bonne réponse
│   ├── wrong.mp3           # Son pour une mauvaise réponse
│   ├── countries_data.txt  # Fichier contenant les données des pays
```

## Format du fichier `countries_data.txt`

Le fichier `resources/countries_data.txt` contient les informations sur les pays sous le format suivant :

```
flag_image, map_image, country_name, capital_name, continent, info_file
```

Exemple :

```
france.png, france_map.png, France, Paris, Europe, france_info.html
```

## Classement en ligne

Le jeu utilise une API PHP hébergée sur `http://studiokatebetpapa.mooo.com` pour enregistrer et afficher les scores des joueurs. Voici comment cela fonctionne :

1. **Envoi du score** : À la fin de chaque partie, le score du joueur est envoyé à l'API.
2. **Récupération du classement** : Le classement des meilleurs scores est récupéré et affiché dans l'application.

### Points d'API utilisés :
- **Ajouter un score** : `POST /Geographie/api/add_score.php`
- **Récupérer le classement** : `GET /Geographie/api/get_scores.php`

## Téléchargement

Découvrez et jouez à **Géographie de Kateb** dès maintenant sur notre site officiel :

[Visitez le site du jeu](https://studiokatebetpapa.rf.gd/nos-jeux/geographie-de-kateb/)

[Télécharger l’APK ici](https://mega.nz/folder/AfVRgToC#sgvyEuivjvNf02A_6bD8KA)

## Pourquoi jouer à Géographie de Kateb ?

- **Éducatif** : Apprenez des faits fascinants sur chaque pays.
- **Personnalisable** : Choisissez un continent ou jouez sur le monde entier.
- **Amusant** : Un moyen interactif d’explorer le monde.
- **Accessible** : Interface intuitive et adaptée aux enfants et adultes.
- **Compétitif** : Comparez vos scores avec ceux des autres joueurs via le classement en ligne.

## Ce qui est prévu pour l’avenir

Nous avons de grandes ambitions pour **Géographie de Kateb**. Voici ce qui est en préparation :

- **Modes avancés** : Augmentation des difficultés et nouveaux types de questions.
- **Expansion des continents** : Ajouter des régions spécifiques (par exemple, Amérique du Nord, Amérique du Sud).
- **Personnalisation** : Ajoutez vos propres thèmes ou questions.
- **Amélioration du classement** : Ajouter des fonctionnalités sociales (amis, défis, etc.).

## Rejoignez-nous

Nous sommes ravis de partager cette aventure avec vous. Vos retours et idées sont essentiels pour améliorer le jeu.

### Contactez-nous

Pour toute question, suggestion ou collaboration, n'hésitez pas à nous contacter :
- **Email** : contact@studiokatebetpapa.com
- **Site web** : [https://studiokatebetpapa.rf.gd](https://studiokatebetpapa.rf.gd)

---

### Notes sur les mises à jour
- **Classement en ligne** : Une nouvelle fonctionnalité permet aux joueurs de comparer leurs scores avec ceux des autres via une API PHP.
- **Sélection des continents** : Les joueurs peuvent choisir un continent spécifique ou jouer sur le monde entier.
- **Correction des continents** : Les continents "Inconnu" ont été corrigés dans le fichier `countries_data.txt`.
- **Amélioration de l'interface** : L'interface a été optimisée pour une meilleure expérience utilisateur.

---

Avec ces mises à jour, **Géographie de Kateb** devient encore plus éducatif, amusant et compétitif. Téléchargez-le dès maintenant et explorez le monde tout en défiant vos amis ! 🌍