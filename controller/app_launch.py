from model.database.manage_db import ManageDatabase
from model.api.api_data_collection import ApiDataCollection
from model.database.food import Food
from model.database.users import Users
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
                self.application_connection(self.cnx)

            elif enter_user == 2:
                enter_user_invalid = False
                print("Good bye")

            else:
                print("Enter invalid. You have to enter '1' to start the app "
                      "or '2' to leave.")

    def application_connection(self, cnx):
        # Opening the welcome window
        print("To use the app you must login or create an account")
        print("Enter 1 to login to your user account")
        print("Enter 2 to create an account")

        enter_user_invalid = True

        while enter_user_invalid:
            enter_user = int(
                input("Enter the number that matches your choice : "))
            if enter_user == 1:
                enter_user_invalid = False
                print("login")
                pseudo_user = input("Enter your pseudo : ")
                print(pseudo_user)
                password_user = input("Enter your password : ")
            elif enter_user == 2:
                enter_user_invalid = False
                print("create a user account")
                email_user = input("Enter your Email : ")
                pseudo_user = input("Enter your pseudo : ")
                password_user = input("Enter your password : ")
                confirm_password_user = input("confirm your password : ")
                # if 'password_user' corresponds to 'confirm_password_user'
                if password_user == confirm_password_user:
                    cursor = self.cnx.cursor()
                    users = Users(cnx, cursor)
                    # Create an account for the new user
                    users.create_user(email_user, pseudo_user, password_user)
                    # send a confirmation email for the creation of the account
                    pass
            else:
                print("Enter invalid. You have to enter '1' to login "
                      "or '2' to create a user account.")
    # @staticmethod
    # def connection_window_opening():
    #     cnx_window = ViewHomeConnect()
    #     ViewHomeConnect.create_widgets(cnx_window)
