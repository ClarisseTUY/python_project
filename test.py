import requests
import concurrent.futures
import outils
def get_station_info(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()

        results = data.get("results", [])
        for result in results:
            # Ajoutez des déclarations print pour déboguer

            station_info = {
                
                "ville": result.get("ville", "N/A"),
                "horaires": result.get("horaires", "N/A"),
                "coordonnees": (result.get("geom", {}).get("lat", "N/A"), result.get("geom", {}).get("lon", "N/A")),
                "region": result.get("reg_name", "N/A"),
                "prices": []  # Initialisez la liste des prix comme une liste vide
            }

            prices = result.get("prix", [])
            if isinstance(prices, list):  # Vérifiez si "prices" est une liste
                for price_info in prices:
                    fuel_name = price_info.get("prix_nom", "N/A")
                    fuel_price = price_info.get("prix_valeur", "N/A")
                    station_info["prices"].append({"carburant": fuel_name, "prix": fuel_price})

            # Ajoutez une déclaration print pour afficher les informations de la station
            print("Station Info:", station_info)

            return station_info
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Reste du code inchangé...


url_api = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?"

# Liste des URLs pour récupérer les prix des carburants
urls = []
for i in range(0, 9899, 100):
    urls.append(outils.nom_url(url_api, 100, i))

# Utilisation de concurrent.futures pour envoyer des requêtes simultanées
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Récupération des résultats
    results = list(executor.map(get_station_info, urls))

# Affichage des résultats dans un tableau
print("Informations des stations:")
print("| Index | Ville | Horaires | Coordonnées | Région | Carburant | Prix |")
print("|-------|-------|----------|-------------|--------|-----------|------|")

for index, station_info in enumerate(results, start=1):
    for price_info in station_info["prices"]:
        print(f"|   {index}   | {station_info['ville']} | {station_info['horaires']} | {station_info['coordonnees']} | {station_info['region']} | {price_info['carburant']} | {price_info['prix']} |")
