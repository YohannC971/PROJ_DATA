import csv

def lire_fichier_entree(nom_fichier):
    lignes = []
    with open(nom_fichier, 'r', newline='') as fichier:
        reader = csv.reader(fichier, delimiter=';', quoting=csv.QUOTE_ALL)  
        for ligne in reader:
            lignes.append(ligne)
    return lignes

def ecrire_fichier_sortie(lignes, nom_fichier_sortie, entete):
    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie, delimiter=';', quoting=csv.QUOTE_ALL) 
        writer.writerow(entete)
        for ligne in lignes:
            writer.writerow(ligne)

def filtrer_lignes_contenant_971(lignes):
    lignes_filtrees = [ligne for ligne in lignes if ligne[0].startswith("971")]
    return lignes_filtrees

def main():
    nom_fichier_entree = 'donnee-data.gouv-2023-geographie2023-produit-le2024-03-07.csv'
    nom_fichier_sortie = 'fichier_filtrage.csv'

    lignes = lire_fichier_entree(nom_fichier_entree)
    entete = lignes[0]  # Première ligne est l'entête
    lignes = lignes[1:]  # Supprime l'entête des lignes à filtrer
    lignes_filtrees = filtrer_lignes_contenant_971(lignes)
    ecrire_fichier_sortie(lignes_filtrees, nom_fichier_sortie, entete)

if __name__ == "__main__":
    main()
