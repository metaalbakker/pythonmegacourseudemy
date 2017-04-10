import folium
import pandas
import os

df=pandas.read_csv('datafiles/Volcanoes-USA.txt')

map = folium.Map(location=[45.372, -121.697], zoom_start=12, tiles='Stamen Terrain')


for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']): #zip de arrays om over de setjes te itereren#
    folium.Marker([lat,lon], popup=name,icon = folium.Icon(color ='red',icon='cloud')).add_to(map)


map.save('test_script2.html')
