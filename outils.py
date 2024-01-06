import api

def initialiser_donnees(url_api, pas=100, limite=9899):
    """
    Initialise les données en effectuant des requêtes simultanées vers l'API.

    Args:
    - url_api (str): URL de l'API pour récupérer les données.
    - pas (int): Pas pour les requêtes par lots.
    - limite (int): Limite pour le nombre total de résultats.

    Returns:
    Tuple de listes initialisées (longitude, latitude, coordonnees, noms_villes, nom_carburant, prix_carburant, prix_id, horaires, adresse).
    """
    longitude, latitude, coordonnees, noms_villes, nom_carburant, prix_carburant, prix_id, horaires, adresse = ([] for _ in range(9))
    urls = [nom_url(url_api, pas, i) for i in range(0, limite, pas)]

    # Demande simultanée pour accéder aux données
    api.requetes_simultanees(urls, longitude, latitude, coordonnees, noms_villes, nom_carburant, prix_carburant, prix_id, horaires, adresse)

    return longitude, latitude, coordonnees, noms_villes, nom_carburant, prix_carburant, prix_id, horaires, adresse


def moyenne(tableau):
    """
    Calcule la moyenne d'un tableau de valeurs numériques.

    Args:
    - tableau (list): Liste des valeurs numériques pour calculer la moyenne.

    Returns:
    float: La moyenne des valeurs du tableau.
    """
    return sum(tableau) / len(tableau) if tableau else None

def maximum(tableau):
    """
    Trouve la valeur maximale dans un tableau de nombres.

    Args:
    - tableau (list): Liste des valeurs numériques.

    Returns:
    int: La valeur maximale dans le tableau.
    """
    tableau_entiers = [int(valeur) if valeur.isdigit() else 0 for valeur in tableau]
    return max(tableau_entiers)

def nom_url(url, limite, debut):
    """
    Génère une URL avec une limite et un point de départ donnés.

    Args:
    - url (str): URL de base.
    - limite (int): Limite pour la requête.
    - debut (int): Point de départ pour la requête.

    Returns:
    str: URL complète avec les paramètres fournis.
    """
    return f"{url}limit={limite}&start={debut}"

def tab_carburants(prix_carburant, nom_carburant):
    """
    Crée un dictionnaire de tableaux de prix de carburants associés à leur nom.

    Args:
    - prix_carburant (list): Liste des prix des carburants.
    - nom_carburant (list): Liste des noms des carburants.

    Returns:
    dict: Dictionnaire avec les noms des carburants comme clés et les tableaux de prix comme valeurs.
    """
    tableaux_carburants = {}

    for carburant, prix in zip(nom_carburant, prix_carburant):
        if carburant == '':
            continue

        # Utiliser setdefault pour éviter la vérification manuelle
        tableaux_carburants.setdefault(carburant, []).append(prix)

    return tableaux_carburants

def moy_carburants(prix_carburant, nom_carburant):
    """
    Calcule les moyennes des prix des carburants.

    Args:
    - prix_carburant (list): Liste des prix des carburants.
    - nom_carburant (list): Liste des noms des carburants.

    Returns:
    dict: Dictionnaire des moyennes des prix pour chaque carburant.
    """
    tableaux_carburants = tab_carburants(prix_carburant, nom_carburant)

    moyennes_carburants = {carburant: moyenne(tableau) for carburant, tableau in tableaux_carburants.items()}

    return moyennes_carburants
