import folium
from folium.plugins import MarkerCluster

def carte(coordonnees):
    coords = (46.539758, 2.430331)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6)
    marker_cluster=MarkerCluster().add_to(map)
    for element in coordonnees:
        # Vérifier la validité des coordonnées
        if len(element) == 2:
            folium.Marker(location=element, popup="Coucou").add_to(marker_cluster)
        else:
            continue

    map.save(outfile='map.html')
    