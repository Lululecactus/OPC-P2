import csv
import os
from scraper import extraire_donnees, extraire_liens_categorie, extraire_toutes_les_categories

url_accueil = "https://books.toscrape.com/index.html"

#récupère toutes les catégories
print("Récupération de la liste des catégories...")
liste_categories = extraire_toutes_les_categories(url_accueil)
total_categories = len(liste_categories)

for i, cat in enumerate(liste_categories, 1):
    nom_cat = cat["nom"]
    url_cat = cat["url"]
    nom_propre = nom_cat.replace("\n", "").replace(" ", "")
    
    print(f"\n[{i}/{total_categories}] Categorie : {nom_propre}")
    
    # Création des dossiers catego
    chemin_dossier = os.path.join("datas", nom_propre)
    os.makedirs(chemin_dossier, exist_ok=True)
    nom_csv = os.path.join(chemin_dossier, f"{nom_propre}.csv")
    
    liens_livres = extraire_liens_categorie(url_cat)
    total_livres = len(liens_livres)
    
    # Écriture du CSV 
    with open(nom_csv, "w", newline="", encoding="utf-8-sig") as f:
        premier_livre = extraire_donnees(liens_livres[0])
        writer = csv.DictWriter(f, fieldnames=premier_livre.keys())
        writer.writeheader()
        
        for j, lien in enumerate(liens_livres, 1):
            print(f"   -> Livre {j}/{total_livres}", end="\r")
            infos = extraire_donnees(lien)
            writer.writerow(infos)
        
        print("")

print("\nExtraction terminée avec succès !")