import requests


class ApiDataCollection:
    """class that allows you to retrieve data from the OpenFoodFact API
    in json file"""

    def __init__(self):
        self.all_products = []
        self.categories = []
        self.name = []
        self.brand = []
        self.store = []
        self.nutriscore = []
        self.url = []
        self.product = []

    def download_data_api(self):
        """Download data to REST d'API Openfoodfacts and insert data into the
        corresponding tables"""
        keys = ['categories', 'generic_name_fr', 'brands', 'stores',
                'nutrition_grade_fr', 'url']
        # Address OpenFooFact
        api = "https://fr.openfoodfacts.org/cgi/search.pl?"

        payload = {"search_terms": "pays",
                   "search_tag": "france",
                   "sort_by": "nom_produit",
                   "page_size": 1000,
                   "json": 1}

        res = requests.get(api, params=payload)
        # Return the response in JSON
        results = res.json()

        # Recording the result in a variable
        products = results["products"]

        # loop for data import and recovery that interests us
        for element in products:
            if keys[0] in element and keys[1] in element \
                    and keys[2] in element and keys[3] in element \
                    and keys[4] in element and keys[5] in element:
                self.categories = [element['categories']]
                self.name = element['generic_name_fr']
                self.brand = [element['brands']]
                self.store = [element['stores']]
                self.nutriscore = element['nutrition_grade_fr']
                self.url = element['url']
                self.product = [self.categories, self.name, self.brand,
                                self.store, self.nutriscore, self.url]

                self.all_products.append(self.product)

        return self.all_products

    def updated_data(self):
        pass
