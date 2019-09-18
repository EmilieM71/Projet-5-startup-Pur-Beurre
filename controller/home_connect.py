from model.database.manage_db import ManageDatabase
from view.view_home_connect import ViewHomeConnect


class HomeConnect:
    """ This class is responsible for:
        - find out if the base exists,
        - find out if the database data is up to date
        - to insert API data into the database
        - display a hom window with welcome message and ask the user to
        log in """

    def __init__(self):
        pass

    def app_launch(self):
        # create database if not exist
        db = ManageDatabase()
        db.create_db()
        # recherche si la base de données contient les données de l'API
        # Si oui : mettre à jour les données via l'API
        # Sinon télécharger les données de l'API

        # Et afficher la fênetre d'accueil
        self.display_home_window()

    @staticmethod
    def display_home_window():
        """This feature allows the home window to be displayed"""
        # Display the home window
        home_window = ViewHomeConnect()
        home_window.window.mainloop()
