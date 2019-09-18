from model.database.manage_db import ManageDatabase
from view.view_home_connect import ViewHomeConnect


class AppLaunch:

    def __init__(self):
        pass

    def greeting(self):
        print("To use the app you need to have to install MySQL version 8")
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
                db = ManageDatabase()
                ManageDatabase.connection_mysql_db(db)

            elif enter_user == 2:
                enter_user_invalid = False
                print("Good bye")

            else:
                print("Enter invalid. You have to enter '1' to start the app "
                      "or '2' to leave.")

    @staticmethod
    def connection_window_opening():
        cnx_window = ViewHomeConnect()
        ViewHomeConnect.create_widgets(cnx_window)
