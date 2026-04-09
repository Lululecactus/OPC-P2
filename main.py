# libs
import requests
from bs4 import BeautifulSoup
import csv

# URL du site pour les phases 2 et apres : https://books.toscrape.com/
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html" 

# Extraction des données
reponse = requests.get(url)
reponse.encoding = "utf-8"
soup = BeautifulSoup(reponse.text, "html.parser")


titre = soup.find("h1").text
lignes = soup.find_all("tr")
upc = lignes[0].find("td").text
price_excl = lignes[2].find("td").text
price_incl = lignes[3].find("td").text
number_available = lignes[5].find("td").text
description_container = soup.find("div", id="product_description")
product_description = description_container.find_next("p").text
category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()
rating_container = soup.find("p", class_="star-rating")
review_rating = rating_container["class"][1]


# Écriture dans le CSV
header_et_data = [
    ["product_page_url", url],
    ["universal_product_code (upc)", upc],
    ["title", titre],
    ["price_including_tax", price_incl],
    ["price_excluding_tax", price_excl],
    ["number_available", number_available],
    ["product_description", product_description],
    ["category", category],
    ["review_rating", review_rating]
]

with open("datas_livre.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(header_et_data)