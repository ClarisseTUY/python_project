import outils
import carte
import api
from subprocess import Popen
import dashboard
import threading
import multiprocessing
import webbrowser
from threading import Timer

url_api = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?"


#Initialisations des tableaux
longitude = []
latitude = []
carburant = []
coordonnees = []
noms_villes = []
nom_carburant = []
prix_carburant = []
horaires = []
prix_id = []
urls=[]
urls = [outils.nom_url(url_api, 100, i) for i in range(0, 9899, 100)]

api.requetes_simultanees(urls,longitude,latitude,coordonnees,noms_villes,nom_carburant,prix_carburant,prix_id,horaires)

carte.carte(coordonnees, noms_villes, horaires, nom_carburant)

def open_browser():
      webbrowser.open("http://127.0.0.1:8050/")

Timer(1, open_browser).start()  
dashboard.creer_dashboard(prix_carburant, nom_carburant)