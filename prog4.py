import pandas as pd

def combinerfichiers(premier_fichier, code_fichier):
    # Lire le premier fichier CSV
    df_premier = pd.read_csv(premier_fichier)

    # Lire le fichier existant code.csv
    df_code = pd.read_csv(code_fichier)

    # Parcourir chaque année unique dans le premier fichier
    annees = df_premier['annee'].unique()
    for annee in annees:
        # Filtrer les données pour l'année en cours
        df_premier_annee = df_premier[df_premier['annee'] == annee]

        # Fusionner les données avec le fichier code.csv basé sur CODGEO
        df_merged = pd.merge(df_code, df_premier_annee[['CODGEO', 'somme_faits']], on='CODGEO', how='left')

        # Remplacer les valeurs NaN par 0 si nécessaire
        df_merged['somme_faits'] = df_merged['somme_faits'].fillna(0)

        # Sauvegarder dans un nouveau fichier CSV pour chaque année
        output_file = f"code{annee}.csv"
        df_merged.to_csv(output_file, index=False)
        print(f"Fichier {output_file} créé avec succès.")

#Exemple d'utilisation
premier_fichier = "fichier_avec_somme.csv"
code_fichier = "code.csv"
combinerfichiers(premier_fichier, code_fichier)