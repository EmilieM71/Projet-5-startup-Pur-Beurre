from model.database.manage_db import ManageDatabase
from model.api.api_data_collection import ApiDataCollection
from model.database.food import Food
# from view.view_home_connect import ViewHomeConnect


class AppLaunch:

    def __init__(self):
        self.api = ApiDataCollection()
        self.db = ManageDatabase()
        self.cursor = None
        self.cnx = None

    def starting(self):
        # Opening the welcome window
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
                # search if the database exists and create if not exist
                self.db.connection_mysql()
                self.cnx = self.db.cnx
                cursor = self.cnx.cursor()
                # find the presence of data in the food table
                food = Food(self.cnx, cursor)
                food.search_if_data()
                # if presence of data : update data
                if food.presence_food:
                    print("Updating data from the API")
                    pass
                # else download data to REST d'API Open Food Facts and
                # insert data into the corresponding tables
                else:
                    cursor.close()
                    self.cnx.close()
                    print("Please wait while loading data to REST d'API "
                          "Open Food Facts and insert data into database")
                    self.db.insert_api_data_into_tables()

            elif enter_user == 2:
                enter_user_invalid = False
                print("Good bye")

            else:
                print("Enter invalid. You have to enter '1' to start the app "
                      "or '2' to leave.")

    def presence_data(self):

        self.data = False
        return self.data

    def if_database_exist(self, cnx):
        # update date to REST d'API Open Food Facts and insert data into
        # the corresponding tables"""
        print(cnx)
        self.api.updated_data()

    def if_database_not_exist(self, cnx, cursor):
        # create the 'PurBeurre' database from the MPD.sql file
        self.cnx = cnx
        self.cursor = cursor
        self.db.create_db(self.cnx)
        self.cnx = cnx
        self.cursor = cursor
        # Download data to REST d'API Open Food Facts and insert data into
        # the corresponding tables
        print("connection bdd avant ajout données dans table", self.cnx,
              "cursor : ", self.cursor)
        self.db.insert_api_data_into_the_corresponding_tables(self.cnx, self.cursor)

    # @staticmethod
    # def connection_window_opening():
    #     cnx_window = ViewHomeConnect()
    #     ViewHomeConnect.create_widgets(cnx_window)
