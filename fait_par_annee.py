import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Vérification de l'existence du fichier CSV
file_path = 'fichier_traite.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")

# Lecture du fichier CSV nettoyé
try:
    data_cleaned = pd.read_csv(file_path, delimiter=';')
except pd.errors.ParserError:
    raise ValueError(f"Erreur de parsing dans le fichier {file_path}. Veuillez vérifier le délimiteur et le format du fichier.")

# Grouper les données par année et sommer les faits
grouped_data = data_cleaned.groupby(['annee']).agg({'faits': 'sum'}).reset_index()

# Augmenter la taille de la figure
plt.figure(figsize=(16, 10))

# Visualiser le nombre de faits par année
plt.plot(grouped_data['annee'], grouped_data['faits'], label='Nombre de Faits', color='b')

plt.xlabel('Année')
plt.ylabel('Nombre de Faits')
plt.title('Nombre de Faits par Année')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.savefig('nombre_de_faits_par_annee.png', format='png', bbox_inches='tight')
plt.show()

significant_increase = grouped_data[grouped_data['faits'] > 10]
significant_decrease = grouped_data[grouped_data['faits'] < -10] 

# Afficher les années avec des augmentations significatives
print("Augmentations significatives :")
print(significant_increase)

print("Diminutions significatives :")
print(significant_decrease)
