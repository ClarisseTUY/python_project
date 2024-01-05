import folium
from folium.plugins import MarkerCluster
from unidecode import unidecode

def nettoyer_nom_ville(nom_ville):
    return unidecode(nom_ville)

def carte(coordonnees, noms_villes, horaires, nom_carburant, prix_carburant):
    coords = (46.539758, 2.430331)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)
    marker_cluster=MarkerCluster().add_to(map)
    for coord, nom_ville, horaire, carburant, prix in zip(coordonnees, noms_villes, horaires, nom_carburant, prix_carburant):
        # Vérifier la validité des coordonnées
        if len(coord) == 2:
            nom_ville_propre = nettoyer_nom_ville(nom_ville)
            
            contenu_popup = f"<b>{nom_ville_propre}</b><br><br>"
            
            if not horaire:
                contenu_popup += f"Pas d'horaires disponibles<br><br>"
            else:
                horaires_str = ""
                for ouverture, fermeture in horaire:
                    horaires_str += f"{ouverture} - {fermeture}<br>"
                contenu_popup += f"Horaires :<br>{horaires_str}<br><br>"
            
            if carburant:
                contenu_popup += f"Carburant :<br>{carburant}<br><br>" 
            else:
                contenu_popup += "Pas d'information sur les carburants<br><br>"

            if prix:
                contenu_popup += f"Prix :<br>{prix}&euro;<br>"
            else:
                contenu_popup += "Pas d'information sur le prix"
            # Définition de la largeur du popup
            popup = folium.Popup(contenu_popup, max_width=70)  # max_width en pixels
            
            folium.Marker(location=coord, popup=popup).add_to(marker_cluster)
        else:
            continue

    map.save(outfile='map.html')
    