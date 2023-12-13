import requests
import json


def api(url,latitude, longitude, coordonnees, villes):
    
    response = requests.get(url)
    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        # Charger la réponse JSON en tant que dictionnaire
        data = response.json()

        # Récupérer et afficher les informations pour chaque résultat
        for result in data.get("results", []):
            index = 0
            print("-----")
            for key, value in result.items():
                if key == 'services_service':
                    print(f"{key}:")
                    if isinstance(value, list):
                        for service in value:
                            print(f"  - {service}")
                    else:
                        print("  Aucun service disponible.")
                elif key == 'geom' and value is not None:
                    print(f"{key}:")
                    lon = value.get('lon', '')
                    lat = value.get('lat', '')
                    print(f"  Longitude: {lon}, Latitude: {lat}")
                    longitude.append(lon)
                    latitude.append(lat)
                    coordonnees.append((lat,lon))
                elif key == 'rupture' and value is not None:
                    print(f"{key}:")
                    rupture_data = json.loads(value)
                    rupture_id = rupture_data.get("@id", "")
                    rupture_nom = rupture_data.get("@nom", "")
                    rupture_debut = rupture_data.get("@debut", "")
                    rupture_fin = rupture_data.get("@fin", "")
                    print(f"  ID: {rupture_id}, Nom: {rupture_nom}, Début: {rupture_debut}, Fin: {rupture_fin}")
                elif key == 'horaires' and value is not None:
                    print(f"{key}:")
                    horaires_data = json.loads(value)
                    automate_24_24 = horaires_data.get("@automate-24-24", "")
                    jours = horaires_data.get("jour", [])
                    print(f"  Automate 24/24: {automate_24_24}")
                    for jour in jours:
                        jour_nom = jour.get("@nom", "")
                        horaires = jour.get("horaire", [])
                        print(f"  {jour_nom.capitalize()}:")
                        if isinstance(horaires, list):
                            for horaire in horaires:
                                ouverture = horaire.get("@ouverture", "")
                                fermeture = horaire.get("@fermeture", "")
                                print(f"    Ouverture: {ouverture}")
                                print(f"    Fermeture: {fermeture}")
                        else:
                            ouverture = horaires.get("@ouverture", "")
                            fermeture = horaires.get("@fermeture", "")
                            print(f"    Ouverture: {ouverture}")
                            print(f"    Fermeture: {fermeture}")
                elif key == 'ville' and value is not None:      
                    print(f"{key}: {value}")
                    ville = value.get('ville', '')
                    villes.append(ville)
                else :
                    print(f"{key}: {value}")


def moyenne(tableau):
    if not tableau:
        return None  # Retourne None si le tableau est vide pour éviter une division par zéro
    somme = sum(tableau)
    moyenne = somme / len(tableau)
    return moyenne

def nom_url(url, limite, debut):
    return f"{url}limit={limite}&start={debut}"
