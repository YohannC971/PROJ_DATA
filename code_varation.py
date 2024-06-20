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

# Ajustement de la taille de la figure pour le graphique des variations annuelles
plt.figure(figsize=(12, 8))  # Ajuster la taille selon vos besoins

# Visualisation des variations par classe avec des couleurs différentes
for classe in grouped_data['classe'].unique():
    subset = grouped_data[grouped_data['classe'] == classe]
    plt.plot(subset['annee'], subset['variation'], label=classe, color=color_dict[classe])

plt.xlabel('Année')
plt.ylabel('Variation (%)')
plt.title('Variations Annuelles par Type de Fait')

# Déplacement de la légende à l'extérieur du graphique
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.grid(True)
plt.tight_layout()  # Ajuster la disposition pour éviter le chevauchement
plt.savefig('variations_annuelles.png', format='png', bbox_inches='tight')
plt.show()


# Fonction pour créer un tableau à partir d'un DataFrame et l'enregistrer en PNG en format paysage
def save_dataframe_as_image(dataframe, title, filename):
    fig, ax = plt.subplots(figsize=(12, len(dataframe) * 0.5))  # Ajuster la largeur pour format paysage
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=dataframe.values, colLabels=dataframe.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)
    plt.title(title, pad=20)
    plt.savefig(filename, format='png', bbox_inches='tight', orientation='landscape')  # Spécifier l'orientation paysage
    plt.close()

# Identifier les types de faits avec des variations significatives (par exemple, ±10%)
significant_increase = grouped_data[grouped_data['variation'] > 10]
significant_decrease = grouped_data[grouped_data['variation'] < -10]

# Afficher les types de faits avec des variations significatives
print("Augmentations significatives :")
print(significant_increase)

print("Diminutions significatives :")
print(significant_decrease)

# Enregistrer les tableaux des augmentations et diminutions significatives en PNG en format paysage
save_dataframe_as_image(significant_increase, 'Augmentations significatives', 'augmentations_significatives.png')
save_dataframe_as_image(significant_decrease, 'Diminutions significatives', 'diminutions_significatives.png')
