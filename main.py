import csv
import os
import sys 
from scraper import extraire_donnees, extraire_liens_categorie, extraire_toutes_les_categories
from utils import telecharger_image

def main():
    url_accueil = "https://books.toscrape.com/index.html"

    # récupère toutes les catégories
    print("Récupération de la liste des catégories...")
    liste_categories = extraire_toutes_les_categories(url_accueil)

    # scrapping de une seule categorie 
    if len(sys.argv) > 1:
        nom_recherche = sys.argv[1].lower()
        liste_filtree = []
        for categorie in liste_categories:
            if nom_recherche in categorie["nom"].lower():
                liste_filtree.append(categorie)
        liste_categories = liste_filtree
        
        if not liste_categories:
            print(f"Aucune catégorie trouvée pour : {nom_recherche}")
            

    total_categories = len(liste_categories)

    for i, cat in enumerate(liste_categories, 1):
        nom_cat = cat["nom"]
        url_cat = cat["url"]
        nom_propre = nom_cat.replace("\n", "").replace(" ", "")
        
        print(f"\n[{i}/{total_categories}] Categorie : {nom_propre}")
        
        # Création des dossiers catego
        chemin_dossier = os.path.join("datas", nom_propre)
        chemin_images = os.path.join(chemin_dossier, "images")
        os.makedirs(chemin_images, exist_ok=True)
        
        nom_csv = os.path.join(chemin_dossier, f"{nom_propre}.csv")
        
        liens_livres = extraire_liens_categorie(url_cat)
        total_livres = len(liens_livres)
        
        # Écriture du CSV 
        with open(nom_csv, "w", newline="", encoding="utf-8-sig") as f:
            if total_livres > 0:
                premier_livre = extraire_donnees(liens_livres[0])
                writer = csv.DictWriter(f, fieldnames=premier_livre.keys())
                writer.writeheader()
                
                for j, lien in enumerate(liens_livres, 1):
                    print(f"   -> Livre {j}/{total_livres}", end="\r")
                    infos = extraire_donnees(lien)
                    writer.writerow(infos)
                    
                    # Téléchargement de l'image
                    nom_image = f"{infos['universal_product_code']}.jpg"
                    chemin_final_image = os.path.join(chemin_images, nom_image)
                    telecharger_image(infos["image_url"], chemin_final_image)
            
            print("")

    print("\nExtraction terminée avec succès !")


if __name__ == "__main__":
    main()