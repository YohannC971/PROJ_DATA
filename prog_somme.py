import pandas as pd

def colonne_somme(input_csv, output_csv):
    # Lire le fichier CSV en utilisant ; comme séparateur
    df = pd.read_csv(input_csv, sep=';')
    
    # Vérifier que les colonnes 'CODGEO_2023', 'annee' et 'faits' existent
    if 'CODGEO_2023' not in df.columns or 'annee' not in df.columns or 'faits' not in df.columns:
        raise ValueError("Les colonnes 'CODGEO_2023', 'annee' et 'faits' doivent exister dans le fichier CSV")

    # Calculer la somme des faits en fonction de CODGEO_2023 et annee
    df['somme_faits'] = df.groupby(['CODGEO_2023', 'annee'])['faits'].transform('sum')
    
    # Enregistrer le nouveau fichier CSV en utilisant ; comme séparateur
    df.to_csv(output_csv, sep=';', index=False)


input_csv = 'colonne_supprimer.csv'
output_csv = 'fichier_avec_somme.csv'

colonne_somme(input_csv, output_csv)



