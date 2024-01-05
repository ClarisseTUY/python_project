# python_project

1. User Guide :
Comment déployer et utiliser le dashboard sur une autre machine :

Déploiement :

Liste des prérequis logiciels ou de configuration nécessaires sur la machine cible :
- visual studio
- installer les packages additionnels requis avec la commande suivante : $ python -m pip install -r installation.txt
Lors de l'execution du fichier main.py, le dashboard s'ouvrira de lui même sur une page web.  

Utilisation :

Le dashboard est constitué de deux onglets : carte et histogramme
Pour accéder à l'un des deux il suffit de cliquer sur l'un des onglets.
Dans l'onglet carte, comme son nom l'indique, on trouvera une carte, dans laquelle nous pouvons observer la répartitions des stations services en France. La carte est interactive, plusieurs informations sont données lorsque l'on clique sur une station. 
Dans l'onglet histogramme, on trouve l'histogramme de la moyenne des prix des carburants. Pour chaque types de carburants, une moyenne des prix est calculée et affichée.

Des captures d'écran ou des exemples pour illustrer l'utilisation.


2. Rapport d'Analyse : 
Les conclusions principales extraites des données :

Introduction :

Contexte de l'analyse : Les stations services en France
Objectifs de l'analyse des données : Proposer une page utilisant des données dynamiques, où les stations sont placées, peuvent être repérée facilement, obtenir des informations sur les horaires, prix des carburants, les types de carburants disponibles, etc..

Analyse des Données :

Principales étapes de l'analyse des données : 
Graphiques (histogramme) et carte qui résument les conclusions.

Principales Conclusions :

Résumé des principales observations tirées des données : Certains endroit possède plusieurs stations, alors que d'autre pas du tout. On constate donc certaines inégalités de répartition. 
Interprétation des tendances ou des points forts : 

3. Developer Guide

Le guide du développeur doit fournir des informations sur l'architecture du code et expliquer comment le modifier ou l'étendre. 

Architecture du Code :

Description de la structure des dossiers et des fichiers.
Explication des composants principaux.

Dépendances :

Liste des dépendances ou bibliothèques utilisées dans le projet : 
requests
folium
plotly-express
dash
dash-core-components
dash-html-components
matplotlib
unidecode

Modification ou Extension :

Instructions pour ajouter de nouvelles fonctionnalités ou modifier des parties spécifiques du code.
Conventions de codage ou recommandations pour maintenir la cohérence du code.