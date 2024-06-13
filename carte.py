import pandas as pd
import folium
from folium.features import DivIcon

# Lire le fichier CSV
file_path = 'code.csv'  # Remplacez par le chemin de votre fichier
df = pd.read_csv(file_path)

# Créer une carte centrée sur la Guadeloupe
m = folium.Map(location=[16.25, -61.55], zoom_start=10)

# Ajouter les communes à la carte avec des encadrés plus petits pour les nombres d'habitants
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        icon=DivIcon(
            icon_size=(100,24),  # Taille de l'icône plus petite
            icon_anchor=(50,12),  # Ancrage de l'icône au centre
            html=f'<div style="font-size: 8pt; border: 1px solid black; background-color: white; padding: 2px;"><b>{row["Commune"]}:</b> {row["nombre_habitants"]} faits</div>'
        )
    ).add_to(m)

# Enregistrer la carte dans un fichier HTML
m.save('carte_guadeloupe.html')

# Afficher la carte
m
