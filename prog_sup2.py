import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("fichier_avec_somme.csv", sep=';')

# Supprimer les colonnes 
df.drop(columns=["millPOP", "LOG", "millLOG"], inplace=True)

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv("fichier_traite.csv",sep=';',  index=False)
