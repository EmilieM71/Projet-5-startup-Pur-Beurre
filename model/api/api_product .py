class ApiProduct:
    """ each product is characterized by several elements:
        - category
        - name
        - brand
        - store
        - nutriscore
        - url """

    def __init__(self):
        self.categories = []
        self.name = []
        self.brand = []
        self.store = []
        self.nutriscore = []
        self.url = []

    def __repr__(self):
        """When we enter our object in the interpreter the method
        modifies the display of the object when it is called"""
        return "[{}, {}, {}, {}, {}, {}]".format(self.category, self.name,
                                                 self.brand, self.store,
                                                 self.nutriscore, self.url)
