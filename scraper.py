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