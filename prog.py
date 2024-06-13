import pandas as pd
from geopy.geocoders import Nominatim
import folium

# Charger les données CSV
data = pd.read_csv('code.csv')

# Initialiser le géocodeur
geocoder = Nominatim(user_agent="mon_application")

# Fonction pour obtenir les coordonnées géographiques à partir du code postal
def get_coordinates(postal_code):
    location = geocoder.geocode(postal_code + ", Guadeloupe")
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Ajouter les coordonnées à la DataFrame
data['latitude'], data['longitude'] = zip(*data['Code Postal'].apply(get_coordinates))

# Supprimer les lignes sans coordonnées
data = data.dropna()

# Créer la carte
carte = folium.Map(location=[16.265, -61.551], zoom_start=10)  # Coordonnées de la Guadeloupe pour le zoom initial

# Ajouter des cercles pour chaque commune avec le nombre d'habitants
for index, row in data.iterrows():
    folium.Circle(
        location=[row['latitude'], row['longitude']],
        radius=row['Nombre habitants'] * 50,  # Ajustez la taille du cercle en fonction du nombre d'habitants
        popup=f"{row['Ville']} - {row['Nombre habitants']} habitants",
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(carte)

# Afficher ou sauvegarder la carte
carte.save('carte_guadeloupe.html')  # Sauvegarde de la carte au format HTML
