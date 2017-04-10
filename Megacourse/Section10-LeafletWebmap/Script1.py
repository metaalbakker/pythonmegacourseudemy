import folium

map = folium.Map(location=[45.372, -121.697], zoom_start=12, tiles='Stamen Terrain')

folium.Marker([45.3288,-121.6625], popup='Mt. Hood Meadows',icon = folium.Icon(color ='red',icon='cloud')).add_to(map)
folium.Marker([45.311,-121,7113], popup='Timberline Lodge',icon = folium.Icon(color ='green')).add_to(map)

map.save('test_script1.html')
