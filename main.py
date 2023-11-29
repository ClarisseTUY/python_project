import requests
import json

api_url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-carburants-fichier-quotidien-test-ods/records?limit=20"

# Effectuer la requête GET
response = requests.get(api_url)

# Vérifier si la requête a réussi (statut 200)
if response.status_code == 200:
    # Charger la réponse JSON en tant que dictionnaire
    data = response.json()

    # Récupérer et afficher les informations pour chaque résultat
    for result in data.get("results", []):
        print("-----")
        for key, value in result.items():
            if key == 'services_service':
                print(f"{key}:")
                if isinstance(value, list):
                    for service in value:
                        print(f"  - {service}")
                else:
                    print("  Aucun service disponible.")
            elif key == 'horaires':
                print(f"{key}:")
                if value:
                    horaires_dict = json.loads(value)
                    horaires = horaires_dict.get('jour', [])
                    for jour in horaires:
                        jour_nom = jour.get('@nom', '')
                        horaire_list = jour.get('horaire', [])
                        if isinstance(horaire_list, list):  # Vérifier si horaire_list est une liste
                            print(f"  {jour_nom}:")
                            for horaire in horaire_list:
                                ouverture = horaire.get('@ouverture', '')
                                fermeture = horaire.get('@fermeture', '')
                                print(f"    {ouverture} - {fermeture}")
                        else:
                            print(f"  {jour_nom}: Aucun horaire disponible.")
                else:
                    print("  Aucun horaire disponible.")
            else:
                print(f"{key}: {value}")

else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")
