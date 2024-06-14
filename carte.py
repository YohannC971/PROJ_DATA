import os
import pandas as pd
import folium
from folium.features import DivIcon
import glob

# Définir les années à traiter
annees = range(16, 24)

# Chemin des fichiers d'entrée et de sortie
input_pattern = os.path.abspath('c:/Users/yohan/OneDrive/Bureau/M1Miage/PROJ DATA/PROJ_DATA/dossierKeny/code_{}_traite.csv')
output_pattern = 'carte_guadeloupe_{}.html'

# Boucler sur chaque année
for annee in annees:
    # Générer le chemin du fichier d'entrée pour l'année actuelle
    file_path = input_pattern.format(annee)
    
    # Lire le fichier CSV
    df = pd.read_csv(file_path, sep=",")

    # Créer une carte centrée sur la Guadeloupe
    m = folium.Map(location=[16.25, -61.55], zoom_start=10)

    # Ajouter les communes à la carte avec des encadrés Bootstrap pour les nombres d'habitants
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            icon=DivIcon(
                icon_size=(150,30),  # Ajustement de la taille de l'icône
                icon_anchor=(75,15),  # Ancrage de l'icône au centre
                html=f'''
                    <div class="card" style="width: 8rem;">
                        <div class="card-body p-2">
                            <h6 class="card-title m-0"><b>{row["Commune"]}</b></h6>
                            <p class="card-text m-0" style="font-size: 8pt;">{row["somme_faits"]} faits</p>
                        </div>
                    </div>
                '''
            )
        ).add_to(m)

    # Ajouter le CSS de Bootstrap à la carte
    bootstrap_css = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
    m.get_root().html.add_child(folium.Element(bootstrap_css))

    # Générer le chemin du fichier de sortie pour l'année actuelle
    output_file = output_pattern.format(annee)

    # Enregistrer la carte dans un fichier HTML
    m.save(output_file)

    # Afficher la carte
    print(f'Carte pour l\'année 20{annee} générée: {output_file}')
