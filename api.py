import requests
import json
import concurrent.futures

def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        results = []
        for result in data.get("results", []):
            result_info = {}
            for key, value in result.items():
                if key == 'geom' and value is not None:
                    lon = value.get('lon', '')
                    lat = value.get('lat', '')
                    result_info['longitude'] = lon
                    result_info['latitude'] = lat
                    result_info['coordonnees'] = (lat, lon)
                elif key == 'horaires' and value is not None:
                    horaires_data = json.loads(value)
                    automate_24_24 = horaires_data.get("@automate-24-24", "")
                    jours = horaires_data.get("jour", [])
                    for jour in jours:
                        jour_nom = jour.get("@nom", "")
                        horaires = jour.get("horaire", [])
                        if isinstance(horaires, list):
                            for horaire in horaires:
                                ouverture = horaire.get("@ouverture", "")
                                fermeture = horaire.get("@fermeture", "")
                        else:
                            ouverture = horaires.get("@ouverture", "")
                            fermeture = horaires.get("@fermeture", "")
                    result_info['automate_24_24'] = automate_24_24
                elif key == 'ville' and value is not None:
                    result_info['ville'] = value
                elif key == 'prix_nom' and value is not None:
                    result_info['nom_carburant'] = value
                elif key == 'prix_valeur' and value is not None:
                    result_info['prix_carburant'] = value
                elif key == 'prix_id' and value is not None :
                    result_info['prix_id']=value

            results.append(result_info)
        #print(results)
        return results

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def requetes_simultanees(urls,longitude,latitude,coordonnees,noms_villes,nom_carburant,prix_carburant,prix_id):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Récupération des résultats
        results = list(executor.map(get_data, urls))

    # Utilisation de concurrent.futures pou
    for result_set in results:
        for result_info in result_set:
            longitude.append(result_info.get('longitude', ''))
            latitude.append(result_info.get('latitude', ''))
            coordonnees.append(result_info.get('coordonnees', ''))
            noms_villes.append(result_info.get('ville', ''))
            nom_carburant.append(result_info.get('nom_carburant', ''))
            prix_carburant.append(result_info.get('prix_carburant', ''))
            prix_id.append(result_info.get('prix_id', ''))