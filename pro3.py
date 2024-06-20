import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("fichier_filtrage.csv", sep=';')

# Supprimer les colonnes 
df.drop(columns=["complementinfoval", "complementinfotaux"], inplace=True)

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv("colonne_supprimer.csv",sep=';',  index=False)
  