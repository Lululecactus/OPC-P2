# libs
import requests
from bs4 import BeautifulSoup
import csv

# URL du site pour les phases 2 et apres : https://books.toscrape.com/
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html" 

# Extraction des données
reponse = requests.get(url)
print(reponse.status_code)
reponse = requests.get(url)
reponse.encoding = "utf-8"
soup = BeautifulSoup(reponse.text, "html.parser")
print(soup)

