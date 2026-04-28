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
    
def telecharger_image(url_image, chemin_complet):
    reponse = requests.get(url_image)
    if reponse.ok:
        with open(chemin_complet, "wb") as f:
            f.write(reponse.content)