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

# Grouper les données par classe et année et sommer les faits
grouped_data = data_cleaned.groupby(['classe', 'annee']).agg({'faits': 'sum'}).reset_index()

# Définir une liste de couleurs uniques pour chaque classe
colors = plt.cm.tab20(np.linspace(0, 1, len(grouped_data['classe'].unique())))

# Créer un dictionnaire de couleurs pour chaque classe
color_dict = {classe: color for classe, color in zip(grouped_data['classe'].unique(), colors)}

# Augmenter la taille de la figure
plt.figure(figsize=(16, 10))  # Ajuster la taille selon vos besoins

# Visualiser le nombre de faits par classe avec des couleurs différentes
for classe in grouped_data['classe'].unique():
    subset = grouped_data[grouped_data['classe'] == classe]
    plt.plot(subset['annee'], subset['faits'], label=classe, color=color_dict[classe])

plt.xlabel('Année')
plt.ylabel('Nombre de Faits')
plt.title('Nombre de Faits par Classe et Année')

# Déplacer la légende à l'extérieur du graphique
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.grid(True)
plt.tight_layout()  # Ajuster la disposition pour éviter le chevauchement
plt.savefig('nombre_de_faits_par_classe.png', format='png', bbox_inches='tight')
plt.show()

# Identifier les types de faits avec des augmentations significatives (par exemple, plus de 10 faits)
significant_increase = grouped_data[grouped_data['faits'] > 10]
significant_decrease = grouped_data[grouped_data['faits'] < -10]  # Note: vérifiez si cela a un sens dans votre contexte

# Afficher les types de faits avec des augmentations significatives
print("Augmentations significatives :")
print(significant_increase)

print("Diminutions significatives :")
print(significant_decrease)
