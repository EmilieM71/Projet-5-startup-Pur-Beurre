import requests
from config.config_db import CATEGORIES


class ApiDataCollection:
    """class that allows you to retrieve data from the OpenFoodFact API
    in json file"""

    def __init__(self):
        pass

    def download_data_api(self):
        """Download data to REST d'API Openfoodfacts and insert data into the
        corresponding tables"""
        # Open API .json Categories data
        payload = {"search_terms": "Boisson",
                   "search_tag": "catégories",
                   "sort_by": "nom_produit",
                   "page_size": 20,
                   "json": 1}
        res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?",
                           params=payload)
        results = res.json()
        print(results["count"])
        products = results["products"]
        print(products)
        # Boucle pour importer les données

        # Insérer des données dans les tables

    def updated_data(self):
        pass
