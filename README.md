# Géographie de Kateb

## Description

**Géographie de Kateb** est un jeu interactif éducatif visant à aider les joueurs à améliorer leurs connaissances en géographie. Le jeu met au défi les joueurs d'identifier des pays à partir de leurs drapeaux, puis de deviner leurs capitales.

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

## Fonctionnalités principales

- **Apprentissage par les drapeaux et les cartes** : Identifiez les pays à partir de leurs drapeaux et explorez leurs cartes.
- **Informations complètes** : Obtenez des détails sur la superficie, la population, la monnaie et plus encore.
- **Scores interactifs** : Suivez vos résultats et progressez à chaque partie.

## Installation

### Prérequis

Avant d'exécuter le jeu, assurez-vous d'avoir :

- **Python 3.8+** installé sur votre machine
- Les bibliothèques suivantes installées :
  ```sh
  pip install  briefcase
  ```

### Clôner le projet

Vous pouvez également retrouver le code source sur GitHub : [GitHub - Géographie de Kateb](https://github.com/kattouba/GeographieKateb)

```sh
https://github.com/kattouba/GeographieKateb
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
flag_image, map_image, country_name, capital_name, info_file
```

Exemple :

```
france.png, france_map.png, France, Paris, france_info.html
```

## Téléchargement

Découvrez et jouez à **Géographie de Kateb** dès maintenant sur notre site officiel :

[Visitez le site du jeu](https://studiokatebetpapa.rf.gd/nos-jeux/geographie-de-kateb/)

[Télécharger l’APK ici](https://mega.nz/file/lW00nRqZ#Z7doCt4Lf7dExuNpt8e_iDXJWTTzNEVIbO3Cguf51r4) Découvrez et jouez à **Géographie de Kateb** dès maintenant !


## Pourquoi jouer à Géographie de Kateb ?

- **Éducatif** : Apprenez des faits fascinants sur chaque pays.
- **Amusant** : Un moyen interactif d’explorer le monde.
- **Accessible** : Interface intuitive et adaptée aux enfants et adultes.

## Ce qui est prévu pour l’avenir

Nous avons de grandes ambitions pour **Géographie de Kateb**. Voici ce qui est en préparation :

- **Modes avancés** : Augmentation des difficultés et nouveaux types de questions.
- **Classements** : Comparez vos scores avec vos amis.
- **Personnalisation** : Ajoutez vos propres thèmes ou questions.

## Rejoignez-nous

Nous sommes ravis de partager cette aventure avec vous. Vos retours et idées sont essentiels pour améliorer le jeu.

### Contactez-nous

