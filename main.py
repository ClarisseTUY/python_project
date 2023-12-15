import outils
import carte
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
urls=[]

#nombre_occurence=outils.api_nombre(url_api)
for i in range(0, 9899, 100):
    urls.append(outils.nom_url(url_api,100,i))
    #outils.api(url,latitude, longitude,coordonnees,villes,nom_carburant,prix_carburant)
    #print(url)

#outils.api(api_url_2,latitude, longitude,coordonnees)
#outils.api(api_url_3,latitude, longitude,coordonnees)  
#carte.carte(coordonnees)

#print(villes)
print(urls)
print(len(urls))
#dashboard.run_server(debug=True)