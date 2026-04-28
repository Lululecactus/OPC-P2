import requests

def clean_price(texte_prix):
    prix_propre = texte_prix.replace("£", "")
    return float(prix_propre)

def clean_available(texte_stock):
    chiffres = ""
    for caractere in texte_stock:
        if caractere.isdigit():
            chiffres = chiffres + caractere
    if chiffres != "":
        return int(chiffres)
    else:
        return 0
    # transsforme les etoile en chiffres poru les review
def convert_rating(texte_rating):
    correspondance = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return correspondance.get(texte_rating, 0)
    
def telecharger_image(url_image, chemin_complet):
    reponse = requests.get(url_image)
    if reponse.ok:
        with open(chemin_complet, "wb") as f:
            f.write(reponse.content)