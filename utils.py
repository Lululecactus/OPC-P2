#  enlève le symbole  du prix et garde le chiffre
def clean_price(texte_prix):
    return float(texte_prix.replace("£", ""))


# Enlève le texte et garde le chiffre de la quantité du stock
def clean_available(texte_stock):
    chiffres = ""
    for caractere in texte_stock:
        if caractere.isdigit():
            chiffres = chiffres + caractere
    if chiffres != "":
        resultat = int(chiffres)
        return resultat
    else:
        return 0
