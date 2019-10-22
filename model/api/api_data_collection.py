import requests
from config.config_db import CATEGORIES


class ApiDataCollection:
    """class that allows you to retrieve data from the OpenFoodFact API
    in json file"""

    def __init__(self):
        self.all_cat_products =[]
        self.all_products = []
        self.categories = []
        self.name = []
        self.brand = []
        self.store = []
        self.nutriscore = []
        self.url = []
        self.last_modified = []
        self.code = []
        self.product = []

    def download_data_api(self):
        """Download data to REST d'API Openfoodfacts and insert data into the
        corresponding tables"""
        keys = ['categories', 'product_name_fr', 'brands', 'stores',
                'nutrition_grade_fr', 'url', 'last_modified_t', 'code']
        # Address OpenFooFact
        api = "https://fr.openfoodfacts.org/cgi/search.pl?"
        for cat in CATEGORIES:
            pages = [1, 2, 3, 4, 5]
            for page in pages:
                payload = {"action": "process",
                           "tagtype_0": "categories",
                           "tag_contains_0": "contains",
                           "tag_0": cat,
                           "tagtype_1": "purchase_places",
                           "tag_contains_1": "contains",
                           "tag_1": "france",
                           "sort_by": "unique_scans_n",
                           "page_size": 1000,
                           "page": page,
                           "json": 1}



        # for cat in CATEGORIES:
        #     payload = {"search_terms": "categorie",
        #                "search_tag": cat,
        #                "sort_by": "nom_produit",
        #                "page_size": 1000,
        #                "json": 1}
        #
        #   res = requests.get(api, params=payload)
                res = requests.get(api, params=payload)
                # Return the response in JSON
                results = res.json()

                # Recording the result in a variable
                products = results["products"]

                # loop for data import and recovery that interests us
                for element in products:
                    if keys[0] in element and keys[1] in element \
                            and keys[2] in element and keys[3] in element \
                            and keys[7] in element:
                        self.categories = [element['categories']]
                        self.name = element['product_name_fr']
                        self.brand = [element['brands']]
                        self.store = [element['stores']]
                        if keys[4] in element:
                            self.nutriscore = element['nutrition_grade_fr']
                        else:
                            self.nutriscore = None
                        if keys[5] in element:
                            self.url = element['url']
                        else:
                            self.url = None
                        if keys[6] in element:
                            self.last_modified = element['last_modified_t']
                        else:
                            self.last_modified = None
                        self.code = int(element['code'])
                        self.product = [self.categories, self.name, self.brand,
                                        self.store, self.nutriscore, self.url,
                                        self.last_modified, self.code]
                self.all_products.append(self.product)
            print("nb d'éléments dans liste cat : ", len(self.all_products))

        print("nb d'éléments dans all_product : ", len(self.all_products))
        return self.all_products

    def update_data(self):
        pass
