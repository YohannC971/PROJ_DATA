import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("test.csv", sep=';')

# Supprimer les colonnes 
df.drop(columns=["complementinfoval", "complementinfotaux"], inplace=True)

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv("nouveau_nom_du_fichier.csv",sep=';',  index=False)
  