import requests
from bs4 import BeautifulSoup
from utils import clean_price, clean_available


# Extraction des données
def extraire_donnees(url):
    reponse = requests.get(url)
    reponse.encoding = "utf-8"
    soup = BeautifulSoup(reponse.text, "html.parser")

    titre = soup.find("h1").text
    lignes = soup.find_all("tr")
    upc = lignes[0].find("td").text
    price_excl = clean_price(lignes[2].find("td").text)
    price_incl = clean_price(lignes[3].find("td").text)
    number_available = clean_available(lignes[5].find("td").text)
    description_container = soup.find("div", id="product_description")
    product_description = description_container.find_next("p").text if description_container else "N/A"
    category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()
    rating_container = soup.find("p", class_="star-rating")
    review_rating = rating_container["class"][1]
    image_url = soup.find("img")["src"].replace("../../", "https://books.toscrape.com/")
    donnees = {
        "product_page_url": url,
        "universal_product_code": upc,
        "title": titre,
        "price_including_tax": price_incl,
        "price_excluding_tax": price_excl,
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url
    }
    
    return donnees


# récupérer les liens de la catégorie
def extraire_liens_categorie(url_categorie):
    liens_livres = []
    url_actuelle = url_categorie

    while url_actuelle != "":
        reponse = requests.get(url_actuelle)
        soup = BeautifulSoup(reponse.text, "html.parser")

        # on recupere les liens de tous les livres par oage
        tous_les_h3 = soup.find_all("h3")
        for h3 in tous_les_h3:
            lien_relatif = h3.find("a")["href"]
            lien_complet = lien_relatif.replace("../../../", "https://books.toscrape.com/catalogue/")
            liens_livres.append(lien_complet)

        #cas il y a une page suivante
        bouton_suivant = soup.find("li", class_="next")
        if bouton_suivant:
            page_suivante = bouton_suivant.find("a")["href"]
            base_url = url_categorie.replace("index.html", "")
            url_actuelle = base_url + page_suivante
        else:
            url_actuelle = ""
            
    return liens_livres