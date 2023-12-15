import folium

def carte(coordonnees):
    coords = (46.539758, 2.430331)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6)

    for element in coordonnees:
        # Vérifier la validité des coordonnées
        if len(element) == 2:
            folium.Marker(location=element, popup="Coucou").add_to(map)
        else:
            continue

    map.save(outfile='map.html')