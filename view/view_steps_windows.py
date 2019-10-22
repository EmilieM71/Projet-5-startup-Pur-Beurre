from model.view.model import ViewModel
from model.database.manage_db import ManageDatabase
from config.config_db import DB_NAME
from model.database.food import Food
from tkinter import *


class ViewStepsWindows:

    def __init__(self):
        self.db = ManageDatabase()
        self.text_step3 = None
        self.text_step6 = None
        self.window = Tk()
        self.window.title(" Pur Beurre ")
        self.window.geometry("480x600")
        self.window.minsize(480, 480)
        # self.window.iconbitmap(" logo.ico ")
        self.window.config(background='white')
        # Create frame in window
        self.frame = Frame(self.window, bg='white')
        self.model = ViewModel(self.frame)

        # creating window components
        self.create_widgets()

        # display
        self.frame.pack(expand=YES)

    def create_widgets(self):

        # create and display text : "APP Lauch"
        self.model.create_text("App launch", ("Arial", 8), 'white', 'black', 1,
                               'w')
        # Step 1- connection to the MySQL
        self.db.connection_mysql()
        # create and display text : "Step 1"
        self.model.create_text("Step 1 : connection to the MySQL",
                               ("Arial", 10), 'white', 'black', 2, 'w')


        # If connection OK self.db.text2 = "You are connected to MySQL"
        #    -> We go to step 2
        # Else Pb connection self.db.text2 = "Something is wrong with your
        #    user name or password"
        #    -> Stop

        # create and display text mysql login information
        self.model.create_text(self.db.text_connect_mysql,
                               ("Arial", 8), 'white', 'black', 3, 'w')

        # Step 2- Search if DB_NAME database exists
        # create and display text : "Step 2"
        self.model.create_text("Step 2 : Search if {} database exists"
                               .format(DB_NAME),
                               ("Arial", 10), 'white', 'black', 4, 'w')
        # If connection OK self.db.text3 = "The DB_NAME database exists"
        #    -> We go to step 3 : Connection DB_NAME Database
        # Else Pb connection self.text3 = "Database DB_NAME does not exists."
        #    -> We go to step 3b : Create DB_NAME Database

        # create text : (text, font_size, wraplength, bg, fg, row, sticky)
        self.model.create_text(self.db.text_search_if_db_exist, ("Arial", 8),
                               'white', 'black', 5, 'w')
        # Step 3
        if self.db.text_search_if_db_exist == "The PurBeurre database exists.":
            # Step 3 = Connection DB_NAME Database
            self.text_step3 = "Step 3 : Connection {} Database".format(DB_NAME)

        elif self.db.text_search_if_db_exist == "Database PurBeurre does " \
                                                "not exists.":
            # Step 3 = "Create DB_NAME Database
            self.text_step3 = "Step 3 : Create {} Database".format(DB_NAME)

        # create and display text : "Step 3"
        self.model.create_text(self.text_step3, ("Arial", 10), 'white',
                               'black', 6, 'w')

        # create text : (text, font_size, wraplength, bg, fg, row, sticky)
        self.model.create_text(self.db.text_connect_db, ("Arial", 8), 'white',
                               'black', 7, 'w')

        text_step4 = "Step 4 : search the presence or absence of data in " \
                     "the database"
        self.model.create_text(text_step4, ("Arial", 10), 'white',
                               'black', 8, 'w')

        # # Step 5 : search the presence or absence of data in the database
        cursor = self.db.cnx.cursor()
        presence_data = Food(self.db.cnx, cursor)
        presence_data.search_if_data()
        # create text : (text, font_size, wraplength, bg, fg, row, sticky)
        self.model.create_text(presence_data.text_presence_data,
                               ("Arial", 8), 'white', 'black', 9, 'w')

        # Step 6
        if presence_data.text_presence_data == "There is no data in database":
            # Step 6 = Download OpenFoodFacts API Data
            self.text_step6 = "Step 6 : Please wait while you download the " \
                              "OpenFoodFacts API data"
            # self.db.insert_api_data_into_tables()
            self.model.create_text(self.db.text_insert_data_api,
                                   ("Arial", 8), 'white', 'black', 11, 'w')

        elif presence_data.text_presence_data == "There is data in database":
            # Step 6 = Update OpenFoodFacts API Data
            self.text_step6 = "Step 6 = Update OpenFoodFacts API Data"

        # create and display text : "Step 3"
        self.model.create_text(self.text_step6, ("Arial", 10), 'white',
                               'black', 10, 'w')




# There is data in database
# Updating data from the API
