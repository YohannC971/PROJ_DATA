import pandas as pd
import os

# Spécifiez le chemin absolu du fichier CSV
input_file = os.path.abspath('./dossierKeny/code_23.csv')
output_file = os.path.abspath('./code_23_traite.csv')

# Vérifiez si le fichier existe
if not os.path.isfile(input_file):
    print(f"Erreur: Le fichier '{input_file}' n'existe pas.")
else:
    # Charger le fichier CSV
    df = pd.read_csv(input_file, sep=',')

    # Supprimer les lignes doublons
    df_sans_doublons = df.drop_duplicates()

    # Enregistrer le résultat dans un nouveau fichier CSV
    df_sans_doublons.to_csv(output_file, index=False)

    print(f"Les doublons ont été supprimés et le nouveau fichier a été enregistré sous '{output_file}'.")
