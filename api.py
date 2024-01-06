import requests
import json
import concurrent.futures

def process_geom(value):
    """
    Traite la clé 'geom' et extrait la longitude, la latitude et les coordonnées.

    Args:
        value (dict): La valeur associée à la clé 'geom'.

    Returns:
        dict: Dictionnaire contenant 'longitude', 'latitude' et 'coordonnees'.
    """
    if value is not None:
        lon = value.get('lon', '')
        lat = value.get('lat', '')
        return {'longitude': lon, 'latitude': lat, 'coordonnees': (lat, lon)}
    return {}

def process_horaires(value):
    """
    Traite la clé 'horaires' et extrait les informations d'horaire.

    Args:
        value (str): La valeur associée à la clé 'horaires'.

    Returns:
        dict: Dictionnaire contenant 'horaires' et 'automate_24_24'.
    """
    if value is not None:
        horaires_data = json.loads(value)
        automate_24_24 = horaires_data.get("@automate-24-24", "")
        jours = horaires_data.get("jour", [])
        horaires_avec_jours = []

        for jour in jours:
            jour_nom = jour.get("@nom", "")
            horaires = jour.get("horaire", [])

            if isinstance(horaires, list):
                horaires_avec_jours.extend(process_horaire(h, jour_nom) for h in horaires)
            else:
                horaires_avec_jours.append(process_horaire(horaires, jour_nom))

        return {'horaires': horaires_avec_jours, 'automate_24_24': automate_24_24}
    return {}

def process_horaire(horaire, jour_nom):
    """
    Traite un horaire individuel et extrait les informations.

    Args:
        horaire (dict): Informations d'horaire individuelles.
        jour_nom (str): Nom du jour.

    Returns:
        dict: Dictionnaire contenant 'jour', 'ouverture' et 'fermeture'.
    """
    ouverture = horaire.get("@ouverture", "")
    fermeture = horaire.get("@fermeture", "")
    return {'jour': jour_nom.capitalize(), 'ouverture': ouverture, 'fermeture': fermeture}

def get_data(url):
    """
    Récupère des données depuis une URL et les formate en fonction des clés spécifiées.

    Args:
        url (str): URL pour récupérer les données.

    Returns:
        list: Liste contenant les informations formatées extraites de l'URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        results = []
        for result in data.get("results", []):
            result_info = {}
            for key, value in result.items():
                if key == 'geom':
                    result_info.update(process_geom(value))
                elif key == 'horaires':
                    result_info.update(process_horaires(value))
                elif key == 'ville' and value is not None:
                    result_info['ville'] = value
                elif key == 'prix_nom' and value is not None:
                    result_info['nom_carburant'] = value
                elif key == 'prix_valeur' and value is not None:
                    result_info['prix_carburant'] = value
                elif key == 'prix_id' and value is not None:
                    result_info['prix_id'] = value
                elif key == 'adresse' and value is not None:
                    result_info['adresse'] = value

            results.append(result_info)

        return results

    except requests.exceptions.RequestException as e:
        print(f"Erreur : {e}")
        return []

def requetes_simultanees(urls, longitude, latitude, coordonnees, villes, nom_carburant, prix_carburant, prix_id, horaires, adresse):
    """
    Effectue des requêtes simultanées vers plusieurs URLs et récupère les informations des résultats.

    Args:
        urls (list): Liste des URLs à requêter.
        longitude (list): Liste pour stocker les longitudes.
        latitude (list): Liste pour stocker les latitudes.
        coordonnees (list): Liste pour stocker les coordonnées.
        villes (list): Liste pour stocker les noms de ville.
        nom_carburant (list): Liste pour stocker les noms des carburants.
        prix_carburant (list): Liste pour stocker les prix des carburants.
        prix_id (list): Liste pour stocker les IDs des prix des carburants.
        horaires (list): Liste pour stocker les horaires.
        adresse (list): Liste pour stocker les adresses.

    Returns:
        None
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(get_data, urls))

    for result_set in results:
        for result_info in result_set:
            longitude.append(result_info.get('longitude', ''))
            latitude.append(result_info.get('latitude', ''))
            coordonnees.append(result_info.get('coordonnees', ''))
            villes.append(result_info.get('ville', ''))
            nom_carburant.append(result_info.get('nom_carburant', ''))
            prix_carburant.append(result_info.get('prix_carburant', ''))
            prix_id.append(result_info.get('prix_id', ''))
            horaires.append(result_info.get('horaires', ''))
            adresse.append(result_info.get('adresse', ''))
