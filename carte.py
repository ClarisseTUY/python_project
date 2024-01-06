import folium
from folium.plugins import MarkerCluster
from unidecode import unidecode

def nettoyer_nom_ville(nom_ville):
    """
    Nettoie le nom de la ville en retirant les caractères spéciaux.
    
    Args:
    - nom_ville (str): Le nom de la ville à nettoyer
    
    Returns:
    str: Le nom de la ville nettoyé
    """
    return unidecode(nom_ville)

def nettoyer_adresse(adresse):
    """
    Nettoie le nom de la ville en retirant les caractères spéciaux.
    
    Args:
    - adresse (str): Le nom de la ville à nettoyer
    
    Returns:
    str: Le nom de la ville nettoyé
    """
    return unidecode(adresse)

def afficher_horaires(horaires):
    """
    Crée une chaîne de caractères pour afficher les horaires de manière structurée.
    
    Args:
    - horaires (list): Liste des horaires, chaque horaire est un dictionnaire {'jour': ..., 'ouverture': ..., 'fermeture': ...}
    
    Returns:
    str: Chaîne de caractères représentant les horaires
    """

    # Construire la chaîne de caractères
    horaires_str = "<b>Horaires :</b><br>"

    if not horaires:
        return horaires_str+"Pas d'horaires disponibles<br><br>"

    # Dictionnaire pour stocker les horaires par jour
    horaires_par_jour = {}

    for horaire in horaires:
        jour = horaire.get('jour', '')
        ouverture = horaire.get('ouverture', '').replace('.', 'h')  # Remplacer le point par 'h'
        fermeture = horaire.get('fermeture', '').replace('.', 'h')  # Remplacer le point par 'h'

        # Ajouter les horaires au dictionnaire par jour
        if jour not in horaires_par_jour:
            horaires_par_jour[jour] = []

        horaires_par_jour[jour].append(f"{ouverture}-{fermeture}")

    for jour, horaires_jour in horaires_par_jour.items():
        horaires_str += f"{jour.capitalize()}: {', '.join(horaires_jour)}<br>"

    return horaires_str + "<br>"


def carte(coordonnees, noms_villes, horaires, nom_carburant, prix_carburant, adresse):
    """
    Crée une carte interactive avec des marqueurs pour chaque station service.

    Args:
    - coordonnees (list): Liste de tuples (latitude, longitude) des stations services.
    - noms_villes (list): Liste des noms des villes.
    - horaires (list): Liste des horaires des stations services.
    - nom_carburant (list): Liste des noms des carburants.
    - prix_carburant (list): Liste des prix des carburants.
    - adresse (list): Liste des adresses des stations services.

    Returns:
    Une carte interactive sauvegardée en tant que fichier HTML ('map.html').
    """
    coords = (46.539758, 2.430331)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)
    marker_cluster = MarkerCluster().add_to(map)

    for coord, nom_ville, horaire, carburant, prix, addr in zip(coordonnees, noms_villes, horaires, nom_carburant, prix_carburant, adresse):
        # Vérifier la validité des coordonnées
        if len(coord) == 2:
            nom_ville_propre = nettoyer_nom_ville(nom_ville)
            contenu_popup = f"<span style='font-size: 13px;'><b>{nom_ville_propre}</b></span><br><br>"

            contenu_popup += f"<b>Adresse :</b><br>"
            str_adresse = nettoyer_adresse(addr) if addr else "Pas d'information sur l'adresse"
            contenu_popup += f"{str_adresse}<br><br>"

            contenu_popup += afficher_horaires(horaire)

            contenu_popup += f"<b>Carburant :</b><br>"
            contenu_popup += f"{carburant}<br><br>" if carburant else "Pas d'information sur les carburants<br><br>"

            contenu_popup += f"<b>Prix :</b><br>"
            contenu_popup += f"{prix}&euro;<br>" if prix else "Pas d'information sur le prix"

            # Définition de la largeur du popup
            popup = folium.Popup(contenu_popup, max_width=200)  # max_width en pixels
            
            folium.Marker(location=coord, popup=popup).add_to(marker_cluster)
        else:
            continue

    map.save(outfile='map.html')