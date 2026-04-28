# 📚 Books Scraper

Scraper Python pour extraire les données de tous les livres du site [books.toscrape.com](https://books.toscrape.com).

Pour chaque catégorie, le script génère un fichier CSV contenant les informations de chaque livre et télécharge les images de couverture.

---

## 📁 Structure du projet

```
books-scraper/
├── main.py            # Point d'entrée du programme
├── scraper.py         # Logique d'extraction (livres, catégories, liens)
├── utils.py           # Fonctions utilitaires (nettoyage des données, téléchargement)
├── requirements.txt   # Dépendances Python
└── datas/             # Dossier de sortie (généré automatiquement à l'exécution)
    └── <Categorie>/
        ├── <Categorie>.csv
        └── images/
            └── <upc>.jpg
```

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Lululecactus/OPC-P2.git
cd OPC-P2
```

### 2. Créer et activer le virtual environment

```bash
# Création
python -m venv venv

# Activation — Linux / macOS
source venv/bin/activate

# Activation — Windows
venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🚀 Utilisation

### Scraping complet — toutes les catégories

```bash
python main.py
```

Le script va :

1. Récupérer la liste des **50 catégories** du site
2. Pour chaque catégorie, créer un dossier `datas/<Categorie>/`
3. Extraire les données de chaque livre et les écrire dans un fichier **CSV**
4. Télécharger les **images de couverture** dans le sous-dossier `images/`

### Scraping partiel — une seule catégorie

Il est possible de ne scraper qu'une seule catégorie en passant son nom en argument :

```bash
python main.py <nom_categorie>
```

**Exemples :**

```bash
python main.py travel
python main.py crime
python main.py mystery
```

Si la catégorie n'existe pas, le script l'indique et affiche la liste complète des catégories disponibles :

```
Aucune catégorie trouvée pour : cryme
```

---

## 📄 Données extraites

Chaque fichier CSV contient les colonnes suivantes :

| Colonne | Description |
|---|---|
| `product_page_url` | URL de la page du livre |
| `universal_product_code` | Code UPC unique du livre |
| `title` | Titre du livre |
| `price_including_tax` | Prix TTC (£) |
| `price_excluding_tax` | Prix HT (£) |
| `number_available` | Nombre d'exemplaires en stock |
| `product_description` | Description du livre |
| `category` | Catégorie |
| `review_rating` | Note (1 à 5) |
| `image_url` | URL de l'image de couverture |

---

## 🧱 Dépendances

| Package | Version |
|---|---|
| `beautifulsoup4` | 4.14.3 |
| `requests` | 2.33.1 |
| `soupsieve` | 2.8.3 |

Voir `requirements.txt` pour la liste complète avec les versions épinglées.
