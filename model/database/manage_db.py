# ! / usr / bin / env python3
# codage: utf-8

# Import modules
from mysql import connector
from mysql.connector import errorcode
from config.config_db import HOST, USER, PASSWORD, DB_NAME
from model.api.api_data_collection import ApiDataCollection


class ManageDatabase:
    """ class to manage the database
        - Connection to MySQL
        - Create database

        - exit connection. """

    def __init__(self):
        self.cnx = None

    def connection_mysql_db(self):
        # Creating the object to load or update API data
        data_api = ApiDataCollection()
        # connection MySQL
        config = {
            'host': HOST,
            'user': USER,
            'password': PASSWORD,
            'database': DB_NAME
        }

        try:
            # connection to the MySQL database
            self.cnx = connector.connect(**config)
            print("Connection to the successful database")
            # Updated data
            print("Loading API data into the database")
            ApiDataCollection.updated_data(data_api)

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                print("Creating the database")
                self.create_db()
                print("The database is created")
                print("loading API data into the database")
                ApiDataCollection.download_data_api(data_api)
                print("loading completed")
            else:
                print(err)
        # finally:
        #     # Creating a MySQL cursor
        #     self.cursor = self.cnx.cursor()
        #     return self.cursor

    def connection_mysql(self):
        # connection MySQL
        config = {
            'host': HOST,
            'user': USER,
            'password': PASSWORD,
        }
        try:
            # connection to the MySQL database
            self.cnx = connector.connect(**config)

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

    def create_db(self):
        """ Create database if not exist"""
        try:
            # connection to the MySQL
            self.connection_mysql()
            # Creating database
            script_sql = open('documentation/MPD.sql')
            script_sql_read = script_sql.read()
            cursor = self.cnx.cursor(script_sql_read)
            script_sql.close()
            try:
                cursor.execute("USE {}".format(DB_NAME))
            except connector.Error as err:
                print("Database {} does not exists.".format(DB_NAME))
                return

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur d\'ouverture.')

    def __exit__(self):
        self.cnx.close()
