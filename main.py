import outils
import carte
import api
from subprocess import Popen
import dashboard
import threading
import multiprocessing
import webbrowser
from threading import Timer

#url utilisé pour les données dynamiques
url_api = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?"


#Initialisations des tableaux
longitude = [] #tableau de longitudes
latitude = [] #tableau de latitudes
carburant = [] #tableau de carburants
coordonnees = [] #tableau de coordonnées
noms_villes = [] #tableau des villes
nom_carburant = [] #tableau du noms des carburants
prix_carburant = [] #tableau des prix de carburants
horaires = [] #tableau des horaires d'ouvertures des stations
prix_id = [] #tableau des id des prix des carburants
urls=[] #tableau d'url
urls = [outils.nom_url(url_api, 100, i) for i in range(0, 9899, 100)]

#demande simultanée pour accèder aux données
api.requetes_simultanees(urls,longitude,latitude,coordonnees,noms_villes,nom_carburant,prix_carburant,prix_id,horaires)

#Appel de la carte
carte.carte(coordonnees, noms_villes, horaires, nom_carburant, prix_carburant)

def open_browser():
      """Ouvre le navigateur web à l'adresse locale du dashboard."""
      webbrowser.open("http://127.0.0.1:8050/")

# Lance le timer pour ouvrir le navigateur
Timer(1, open_browser).start()  
dashboard.creer_dashboard(prix_carburant, nom_carburant)