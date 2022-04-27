import folium
import pandas as pd


def color_producer(elevation):
    if elevation > 3000:
        return "green"
    elif elevation<1000:
        return "red"
    else:
        return "orange"


df = pd.read_csv("136 Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elve = list(df["ELEV"])
map = folium.Map(location=[40, -100], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elve):
    fgv.add_child(folium.Marker(location=[lt, ln],popup=str(el) + " m", icon=folium.Icon(color_producer(el))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
    style_function=lambda x: {
        'fillColor': 'green' if x['properties']['POP2005']<1000000
        else 'orange' if 1000000<= x['properties']['POP2005']<10000000
        else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("1.html")
