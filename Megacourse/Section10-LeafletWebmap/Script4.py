import folium
import pandas
import os

def color(elevation):

    col = 'green' if elevation in range(0,1000) else 'orange' if elevation in range(1000,3000) else 'red'
    return col

df=pandas.read_csv('datafiles/Volcanoes-USA.txt')

mean_lat = df['LAT'].mean()
mean_lon = df['LON'].mean()

map = folium.Map(location=[mean_lat, mean_lon], zoom_start=12, tiles='Stamen Terrain')


for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']): #zip de arrays om over de setjes te itereren#

    marker_color = color(elev)

    folium.Marker([lat,lon], popup=name,icon = folium.Icon(color =marker_color,icon='cloud')).add_to(map)


map.save('test_script4.html')



