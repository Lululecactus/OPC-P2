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