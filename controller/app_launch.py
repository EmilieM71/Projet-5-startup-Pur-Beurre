from model.database.manage_db import ManageDatabase
from model.api.api_data_collection import ApiDataCollection
# from view.view_home_connect import ViewHomeConnect


class AppLaunch:

    def __init__(self):
        self.api = ApiDataCollection()
        self.db = ManageDatabase()
        self.my_cursor = None

    def starting(self):
        print("To use the app you need to have to install MySQL version 8, and"
              " create user name :'student_OC', host: 'localhost', "
              "password: '123abc'")
        print("Enter 1 to launch the app")
        print("Tapez 2 to leave")

        enter_user_invalid = True

        while enter_user_invalid:
            enter_user = int(
                input("Enter the number that matches your choice : "))
            if enter_user == 1:
                enter_user_invalid = False
                print("App launch")
                # search if the database exists
                self.search_if_the_database_exists()

            elif enter_user == 2:
                enter_user_invalid = False
                print("Good bye")

            else:
                print("Enter invalid. You have to enter '1' to start the app "
                      "or '2' to leave.")

    def search_if_the_database_exists(self):
        # 1- Connect to mysql
        self.db.connection_mysql()
        # 2- Create my cursor
        self.my_cursor = self.db.cnx.cursor()
        # 3- Connecting to the database "PurBeurre"
        self.db.connect_db(self.my_cursor)
        # If the database does not exist
        if not self.db.connect_db_name:
            self.if_database_not_exist()
            return self.my_cursor
        else:
            self.if_database_exist()

    def if_database_exist(self):
        # update date to REST d'API Open Food Facts and insert data into
        # the corresponding tables"""
        self.api.updated_data()

    def if_database_not_exist(self):
        # create the 'PurBeurre' database from the MPD.sql file
        # (in the 'documentation' packing)
        self.db.create_db(self.my_cursor)
        self.db.connect_db(self.my_cursor)
        # Download data to REST d'API Open Food Facts and insert data into
        # the corresponding tables"""
        self.api.download_data_api()

    # @staticmethod
    # def connection_window_opening():
    #     cnx_window = ViewHomeConnect()
    #     ViewHomeConnect.create_widgets(cnx_window)
