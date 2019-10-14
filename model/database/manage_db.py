# ! / usr / bin / env python3
# codage: utf-8

# Import
from mysql import connector
from mysql.connector import errorcode
from config.config_db import (HOST, USER, PASSWORD, DB_NAME, PATH_FILE)
from model.api.api_data_collection import ApiDataCollection
from model.database.category import Category
from model.database.food import Food
from model.database.category_food import CategoryFood
from model.database.brand import Brand
from model.database.food_brand import FoodBrand
from model.database.store import Store
from model.database.food_store import FoodStore


class ManageDatabase:
    """ class to manage the database
        - Connection to MySQL
        - Connect database DB_NAME if exist, elif create DB
        - Create database
        - exit connection. """

    def __init__(self):
        self.cnx = None
        self.cursor = None

    def connection_mysql(self):
        # connection MySQL
        config = {
            'host': HOST,
            'user': USER,
            'password': PASSWORD
        }
        try:
            # connection to the MySQL
            self.cnx = connector.connect(**config)
            print("You are connected to MySQL")
            # connection to database 'PurBeurre'
            self.connect_db(self.cnx)

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

    def connect_db(self, cnx):
        self.cursor = cnx.cursor()
        try:
            self.cursor.execute("USE {}".format(DB_NAME))
            print("You are connected to {} Database".format(DB_NAME))

        except connector.Error:
            print("Database {} does not exists.".format(DB_NAME))
            # Create database 'PurBeurre'
            self.create_db(cnx)

        else:
            self.cursor.close()
            return self.cnx

    def create_db(self, cnx):
        """ Create database if not exist"""
        self.cursor = cnx.cursor()
        try:
            # Opening the file containing the SQL script
            sql_file = open(PATH_FILE, 'r')
            # Read file
            sql_text = sql_file.read()
            sql_stmts = sql_text.split(';')
            for s in sql_stmts:
                self.cursor.execute(s)
            print("The database is created")
            # Make sure db is committed
            self.cnx.commit()

        except connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

        else:
            self.cursor.close()

    def insert_api_data_into_tables(self):

        # Creating an object for class ApiDataCollection
        data_api = ApiDataCollection()  # Data from api

        # Recover openFoodFacts API data
        data_api.download_data_api()

        # Connection bdd
        cnx = connector.connect(host=HOST, user=USER, password=PASSWORD,
                                database=DB_NAME)
        # # Creating a cursor object
        cursor = cnx.cursor()

        # Creating an object for each class
        food_table = Food(cnx, cursor)  # Table food
        cat_table = Category(cnx, cursor)  # Table category
        cat_food_table = CategoryFood(cnx, cursor)  # table category_food
        brand_table = Brand(cnx, cursor)  # table brand
        food_brand_table = FoodBrand(cnx, cursor)  # table food_brand
        store_table = Store(cnx, cursor)  # Table store
        food_store_table = FoodStore(cnx, cursor)  # Table food_store

        # Insert data into the corresponding tables
        for product in data_api.all_products:
            # Search if the food already exists in the database
            # and if not exist, insert name, nutriscore and url in table food
            food_table.search_if_food_exist(product[1], product[4], product[5])
            id_food = food_table.id
            # Insert category in table category)
            for cat in product[0][0].split(","):
                # Search if the category already exists in the database
                # and if not exist, insert name in table category
                cat_table.search_if_category_exist(cat)
                id_cat = cat_table.category_id
                # Insert id_food and id_cat in table category_food
                cat_food_table.search_if_cat_food_exist(id_cat, id_food)
            # Insert brand in brand table
            for brand in product[2][0].split(","):
                # Search if the brand already exists in the database
                # and if not exist, insert name in table brand
                brand_table.search_if_brand_exist(brand)
                id_brand = brand_table.brand_id
                # Insert id_food and id_brand in food_brand table
                food_brand_table.search_if_food_brand_exist(id_food, id_brand)
            # Insert store in store table
            for store in product[3][0].split(","):
                store_table.search_if_store_exist(store)
                id_store = store_table.store_id
                # Insert id_food and id_store in food_brand table
                food_store_table.search_if_food_store_exist(id_food, id_store)
        cursor.close()
        cnx.close()
        print("The data was inserted into the 'PurBeurre' database")

    def __exit__(self):
        self.cnx.close()
        print("")
