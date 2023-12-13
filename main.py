import outils
import carte

api_url_1 = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=100"
url_api = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?"

api_url_2 = outils.nom_url(url_api,100,100)
print(api_url_2)
api_url_3 = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=100&start=400&offset=30"

#Initialisations des tableaux
longitude = []
latitude = []
carburant = []
coordonnees = []
villes = []

"""for i in range(0, 74000, 100):
    url=outils.nom_url(url_api,100,i*100)
    outils.api(url,latitude, longitude,coordonnees,villes)
#outils.api(api_url_2,latitude, longitude,coordonnees)
#outils.api(api_url_3,latitude, longitude,coordonnees)   
#carte.carte(coordonnees)"""

url=outils.nom_url(url_api,100,7400)
outils.api(api_url_1,latitude, longitude,coordonnees,villes)

print(villes)
