import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lecture du fichier CSV nettoyé
file_path = 'fichier_traite.csv'
data_cleaned = pd.read_csv(file_path, delimiter=';')

# Regroupement des données par classe (type de fait) et année
grouped_data = data_cleaned.groupby(['classe', 'annee']).agg({'faits': 'sum'}).reset_index()

# Calcul des variations annuelles pour chaque type de fait
grouped_data['variation'] = grouped_data.groupby('classe')['faits'].pct_change() * 100

# Remplacement des NaN par 0 pour les premières années où il n'y a pas de changement
grouped_data['variation'].fillna(0, inplace=True)

# Définition d'une liste de couleurs uniques pour chaque classe
colors = plt.cm.tab20(np.linspace(0, 1, len(grouped_data['classe'].unique())))

# Création d'un dictionnaire de couleurs pour chaque classe
color_dict = {classe: color for classe, color in zip(grouped_data['classe'].unique(), colors)}


plt.figure(figsize=(12, 8)) 

# Visualisation des variations par classe avec des couleurs différentes
for classe in grouped_data['classe'].unique():
    subset = grouped_data[grouped_data['classe'] == classe]
    plt.plot(subset['annee'], subset['variation'], label=classe, color=color_dict[classe])

plt.xlabel('Année')
plt.ylabel('Variation (%)')
plt.title('Variations Annuelles par Type de Fait')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.savefig('variations_annuelles.png', format='png', bbox_inches='tight')
plt.show()


# Identifier les types de faits avec des variations significatives (par exemple, ±10%)
significant_increase = grouped_data[grouped_data['variation'] > 10]
significant_decrease = grouped_data[grouped_data['variation'] < -10]

# Afficher les types de faits avec des variations significatives
print("Augmentations significatives :")
print(significant_increase)

print("Diminutions significatives :")
print(significant_decrease)