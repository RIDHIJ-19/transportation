from geopy.geocoders import Nominatim
from geopy import distance

# Initialize the geocoder
geolocator = Nominatim(user_agent="Your Application Name")

# Get the coordinates for Delhi and Bangalore
location1 = start+", India"
location2 = stop +", India"
coordinates1 = geolocator.geocode(location1)
coordinates2 = geolocator.geocode(location2)

# Extract latitude and longitude from the coordinates
lat1, lon1 = coordinates1.latitude, coordinates1.longitude
lat2, lon2 = coordinates2.latitude, coordinates2.longitude

# Calculate the distance between the two points
distance_km = distance.distance((lat1, lon1), (lat2, lon2)).km

# Print the distance in kilometers
print("The distance between ",start," and ",stop,"is:", distance_km, "kilometers")
car = 10  truck = 30 tempo = 45
fcost = distance_km * mode;
print("The distance between ",start," and ",stop,"is:", fcost, "rupees")
