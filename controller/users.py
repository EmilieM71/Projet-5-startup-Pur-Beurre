from view.view_home_connect import ViewHomeConnect


class User:
    """ This class is responsible for :

        - display a hom window with welcome message and ask the user to
        log in """
    def __init__(self):
        pass

    @staticmethod
    def open_home_connect_window():
        """This feature allows the home window to be displayed"""
        # Opening the home connect window
        view_home_connect = ViewHomeConnect()
        view_home_connect.window.mainloop()

    def log_in(self):
        # ouverture fenetre avec formulaire pour se connecter
        # rechercher si les identifiants saisie existe

        pass

    def create_an_account(self):
        # ouverture fenetre de creation de compte
        pass
