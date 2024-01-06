# python_project

1. User Guide :
Comment déployer et utiliser le dashboard sur une autre machine :

Déploiement :

Liste des prérequis logiciels ou de configuration nécessaires sur la machine cible :
- Visual Studio Code installé.
- L'extension Python pour Visual Studio Code installée.

Exécutez le script principal main.py, et le tableau de bord s'ouvrira automatiquement dans un navigateur Web.


Utilisation :

Le tableau de bord est composé de deux onglets : "Carte" et "Histogramme".

Onglet Carte
Cet onglet affiche une carte interactive montrant la répartition des stations-service en France. La carte est interactive, et des informations détaillées sur une station sont affichées lorsqu'elle est sélectionnée.

Onglet Histogramme
Cet onglet affiche un histogramme représentant la moyenne des prix des carburants. Chaque type de carburant est représenté avec sa moyenne de prix.

Menu
Le menu propose des informations sur les auteurs du projet et fournit des détails sur l'API utilisée pour les données dynamiques.


2. Rapport d'Analyse : 

Introduction
Le projet se concentre sur l'analyse des stations-service en France. L'objectif est de fournir un tableau de bord interactif utilisant des données dynamiques pour localiser et obtenir des informations sur les stations.

Analyse des Données
L'analyse se compose principalement d'un histogramme des prix moyens des carburants et d'une carte interactive.

Principales Conclusions
Certaines régions présentent une concentration plus élevée de stations, tandis que d'autres en ont moins, indiquant des inégalités de répartition.


3. Developer Guide

Le guide du développeur doit fournir des informations sur l'architecture du code et expliquer comment le modifier ou l'étendre. 

Architecture du Code :

La structure du code se compose des fichiers suivants :
- main.py : Le fichier principal pour lancer le tableau de bord.
- outils.py : Ce fichier regroupe des fonctions utilitaires essentielles, utilisées dans l'ensemble du programme.
- dashboard.py : Construit le tableau de bord, gère la mise en page, les couleurs, et intègre l'histogramme et la carte.
- carte.py : Crée la carte interactive avec des popups pour chaque station.
- api.py : Récupère les informations de l'API pour remplir les tableaux de données.

Dépendances : 
- requests
- folium
- plotly-express
- dash
- dash-core-components
- dash-html-components
- matplotlib
- unidecode

Modification ou Extension :
Pour ajouter de nouvelles fonctionnalités ou modifier des parties spécifiques du code, suivez les conventions de codage pour maintenir la cohérence.