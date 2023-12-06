import folium

def carte(coordonnees):
    coords = (46.539758, 2.430331)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6)

    for element in coordonnees:
        folium.Marker(location=element, popup = "Coucou").add_to(map)
        map.save(outfile='map.html')
    