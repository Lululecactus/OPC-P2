import requests
from bs4 import BeautifulSoup
from utils import clean_price, clean_available

# Extraire les données d'un livre
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
    
    desc_container = soup.find("div", id="product_description")
    product_description = desc_container.find_next("p").text if desc_container else "N/A"
    
    category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text
    rating_container = soup.find("p", class_="star-rating")
    review_rating = rating_container["class"][1]
    image_url = soup.find("img")["src"].replace("../../", "https://books.toscrape.com/")
    
    return {
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

# Extraire les liens des livres d'une catégorie
def extraire_liens_categorie(url_categorie):
    liens_livres = []
    url_actuelle = url_categorie

    while url_actuelle != "":
        reponse = requests.get(url_actuelle)
        soup = BeautifulSoup(reponse.text, "html.parser")

        tous_les_h3 = soup.find_all("h3")
        for h3 in tous_les_h3:
            lien_relatif = h3.find("a")["href"]
            lien_complet = lien_relatif.replace("../../../", "https://books.toscrape.com/catalogue/")
            liens_livres.append(lien_complet)

        bouton_suivant = soup.find("li", class_="next")
        if bouton_suivant:
            page_suivante = bouton_suivant.find("a")["href"]
            base_url = url_categorie.replace("index.html", "")
            url_actuelle = base_url + page_suivante
        else:
            url_actuelle = ""
            
    return liens_livres

# Extraire la liste de toutes les catégories
def extraire_toutes_les_categories(url_accueil):
    categories = []
    reponse = requests.get(url_accueil)
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    nav_list = soup.find("ul", class_="nav-list").find("ul")
    liens_a = nav_list.find_all("a")
    
    for a in liens_a:
        nom = a.text
        lien_complet = "https://books.toscrape.com/" + a["href"]
        categories.append({"nom": nom, "url": lien_complet})
        
    return categories