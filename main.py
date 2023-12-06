import outils
import carte

api_url_1 = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=100"
api_url_2 = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=100&start=250&offset=30"
api_url_3 = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=100&start=400&offset=30"

#Initialisations des tableaux
longitude = []
latitude = []
carburant = []
coordonnees = []


outils.api(api_url_1,latitude, longitude,coordonnees)
#outils.api(api_url_2,latitude, longitude,coordonnees)
#outils.api(api_url_3,latitude, longitude,coordonnees)   
carte.carte(coordonnees)
