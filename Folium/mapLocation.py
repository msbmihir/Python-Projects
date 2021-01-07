import folium 

my_map3 = folium.Map(location = [28.5011226, 77.4099794], 
										zoom_start = 15) 


folium.Marker([28.5011226, 77.4099794], 
			popup = ' noida ').add_to(my_map3) 


my_map3.save(" my_map3.html ")
