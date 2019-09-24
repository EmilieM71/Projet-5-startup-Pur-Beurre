# ! / usr / bin / env python3
# codage: utf-8

# Import
from mysql import connector
from mysql.connector import errorcode
from config.config_db import HOST, USER, PASSWORD, DB_NAME
# from model.api.api_data_collection import ApiDataCollection


class ManageDatabase:
    """ class to manage the database
        - Connection to MySQL
        - Connect database DB_NAME if exist, elif create DB
        - Create database
        - exit connection. """

    def __init__(self):
        self.cnx = None
        self.cursor = None
        self.connect_db_name = False

    def connection_mysql(self):
        # connection MySQL
        config = {
            'host': HOST,
            'user': USER,
            'password': PASSWORD,
        }
        try:
            # connection to the MySQL
            self.cnx = connector.connect(**config)
            print("You are connected to MySQL")

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

    def connect_db(self, cursor):
        self.cursor = cursor
        try:
            self.cursor.execute("USE {}".format(DB_NAME))
            print("You are connected to 'PurBeurre' Database")
        except connector.Error:
            print("Database {} does not exists.".format(DB_NAME))
            # print(err)
            self.connect_db_name = False
        else:
            self.connect_db_name = True
        return self.connect_db_name

    def create_db(self, cursor):
        """ Create database if not exist"""
        try:
            self.cursor = cursor
            # Opening the file containing the SQL script
            sql_file = open("documentation/MPD.sql", 'r')
            sql_text = sql_file.read()
            sql_stmts = sql_text.split(';')
            for s in sql_stmts:
                print(s)
                cursor.execute(s)
            self.cnx.commit()

        except connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    # def find_if_database_contains_data(self, cursor):
    #     query = " SELECT name FROM category "
    #
    #     self.cursor.execute(query)
    #
    #     # for name in self.cursor:
    #     #     print("{}".format(name))

    def __exit__(self):
        self.cnx.close()
        print("")
