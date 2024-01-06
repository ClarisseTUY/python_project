import subprocess

# Mettre à niveau pip et installer les modules au début du script
subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
subprocess.run(['python', '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)

import outils
import carte
import dashboard
from threading import Timer
import webbrowser

# URL utilisée pour les données dynamiques
url_api = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?"

# Initialisations des tableaux
longitude, latitude, coordonnees, noms_villes, nom_carburant, prix_carburant, prix_id, horaires, adresse = outils.initialiser_donnees(url_api, pas=100, limite=9899)

# Appel de la carte
carte.carte(coordonnees, noms_villes, horaires, nom_carburant, prix_carburant, adresse)


def ouvrir_navigateur():
    """Ouvre le navigateur web à l'adresse locale du dashboard."""
    webbrowser.open("http://127.0.0.1:8050/")

# Lance le timer pour ouvrir le navigateur
Timer(1, ouvrir_navigateur).start()

dashboard.creer_dashboard(prix_carburant, nom_carburant)
