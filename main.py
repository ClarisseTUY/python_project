import outils
import carte
import api
import dashboard

api_url_1 = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=100"
url_api = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?"

api_url_2 = outils.nom_url(url_api,100,100)
api_url_3 = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=100&start=400&offset=30"

#Initialisations des tableaux
longitude = []
latitude = []
carburant = []
coordonnees = []
villes = []
nom_carburant = []
prix_carburant = []
prix_id = []
urls=[]

urls = [outils.nom_url(url_api, 100, i) for i in range(0, 9899, 100)]

api.requetes_simultanees(urls,longitude,latitude,coordonnees,villes,nom_carburant,prix_carburant,prix_id)

carte.carte(coordonnees)


#dashboard.run_server(debug=True)