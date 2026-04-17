# libs
import csv
from scraper import extraire_donnees, extraire_liens_categorie

# 1. URL de la catégorie choisie (ex: Travel)
url_categorie = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# 2. On récupère la liste de tous les liens de cette catégorie
print("Récupération des liens de la catégorie en cours...")
tous_les_liens = extraire_liens_categorie(url_categorie)
print(f"Nombre de livres trouvés : {len(tous_les_liens)}")

nom_fichier = "donnees_categorie_travel.csv"

# 3. Écriture CSV (Ta structure classique avec la boucle)
with open(nom_fichier, "w", newline="", encoding="utf-8-sig") as f:
    # On extrait le 1er livre pour générer les en-têtes automatiquement
    infos_premier_livre = extraire_donnees(tous_les_liens[0])
    en_tetes = infos_premier_livre.keys()
    
    writer = csv.DictWriter(f, fieldnames=en_tetes)
    writer.writeheader() # On écrit les titres une seule fois
    
    # On boucle sur chaque lien pour extraire et écrire les données
    for lien in tous_les_liens:
        print(f"Extraction de : {lien}")
        infos_livre = extraire_donnees(lien)
        writer.writerow(infos_livre)

print(f"Fichier {nom_fichier} créé avec succès !")
