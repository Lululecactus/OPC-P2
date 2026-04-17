# libs
import csv
from scraper import extraire_donnees

url_livre = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
infos_livre = extraire_donnees(url_livre)
nom_fichier = "donnees_livre.csv"

# Écriture CSV
with open(nom_fichier, "w", newline="", encoding="utf-8-sig") as f:
    en_tetes = infos_livre.keys()
    writer = csv.DictWriter(f, fieldnames=en_tetes)
    writer.writeheader()
    writer.writerow(infos_livre)

print(f"Fichier {nom_fichier} créé au format classique !")

