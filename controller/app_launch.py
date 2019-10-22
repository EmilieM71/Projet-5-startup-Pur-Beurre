from view.view_welcome_window import ViewWelcomeWindow
from model.database.manage_db import ManageDatabase
from model.api.api_data_collection import ApiDataCollection
from model.database.food import Food
from model.database.users import Users


class AppLaunch:
    """ This class is responsible for launching the application:
        - open view: welcome with an informational message and 2 buttons
        to launch the application or leave it
        - open view : steps which shows the steps that the application does
        before startup
        - find out if the base exists,
        - find out if the database data is up to date
        - to insert API data into the database
        - display a hom window with welcome message and ask the user to
        log in
        - contains useful functions to act when the user clicks a button
        corresponding to a view
        """
    def __init__(self):
        # Creating an object for each model class used
        self.api = ApiDataCollection()
        self.db = ManageDatabase()
        # Creating an object for each view class used
        # self.view_welcome = ViewWelcomeWindow()

        self.cursor = None
        self.cnx = None

    # def steps_starting_app(self):
    #     """ This function opens the view of the steps performed by the
    #             application before startup """
    #
    #     # Step 1 : connection to MySQL
    #     self.db.connection_mysql()
    #     self.text2 = self.db.text_connect_mysql
    #
    #     # Step 2 : search if database exist.
    #     # if exist
    #     #     Step 3 = connection to database
    #     # else
    #     #     Step 3 = create database and connection
    #
    #     # Step 4 : search if presence date
    #     # if date
    #     #     Step 5 = update data
    #     # else
    #     #     Step 5 = download data API

    # def starting(self):
    #     """ This function :
    #         - opens the welcome view
    #         - when the user press the button "Launch the app", starts opening
    #         the window step"""
    #     # Opening the view welcome
    #     self.view_welcome.window.mainloop()

    def connection_mysql(self):
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

    def starting_console_mode(self):
        # console mode
        print("To use the app you need to have to install MySQL version 8, "
              "and create user name :'student_OC', host: 'localhost', "
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
                print("Enter invalid. You have to enter '1' to start app "
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
                pseudo_user = input("Enter your pseudo : ")
                password_user = input("Enter your password : ")
                cursor = self.cnx.cursor()
                users = Users(cnx, cursor)
                users.search_if_user_exist(pseudo_user, password_user)

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
