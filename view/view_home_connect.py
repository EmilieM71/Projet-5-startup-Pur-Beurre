from model.view.model import ViewModel
from tkinter import *


class ViewHomeConnect:
    """"""

    def __init__(self):
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
        """

        :rtype:
        """
        # create title : (text, font_size, bg, fg, row, sticky)
        self.model.create_title(" Bienvenue ", ("Arial", 40), 'white',
                                '#ADD0EC', 0, 'w')
        # create subtitle : (text, justify, font_size, bg, fg, row, sticky)
        self.model.create_subtitle(" Se connecter ", 'LEFT', ("Arial", 20),
                                   'white', 'black', 1, 'w')
        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 2, 'w')
        # create label and entry (label_text, font_size_label, bg_label,
        # fg_label, label_row, column_lable, sticky_label,
        # font_size_entry, bg_entry, fg_entry, column_entry, sticky_entry)
        self.model.create_label_entry(" Pseudo ", ("Arial", 15), 'white',
                                      'black', 3, 0, 'w', ("Arial", 20),
                                      'white', 'black', 0, 'w')
        # create label and entry (label_text, font_size_label, bg_label,
        # fg_label, label_row, column_lable, sticky_label,
        # font_size_entry, bg_entry, fg_entry, column_entry, sticky_entry)
        self.model.create_label_entry(" Password ", ("Arial", 15), 'white',
                                      'black', 5, 0, 'w', ("Arial", 20),
                                      'white', 'black', 0, 'w')
        # create button : (bd, text, font_size, bg, fg, command, row,
        #                       sticky, pady, underline)
        self.model.create_button(2, " se connecter ", ("Arial", 20), '#ADD0EC',
                                 "white", self.login(), 7, 'w', 20, False)
        # create button : (bd, text, font_size, bg, fg, command, row,
        #                       sticky, pady, underline)
        self.model.create_button(0, " Mot de passe oublié ", ("Arial", 10),
                                 "white", 'blue', self.forgotten_password(),
                                 8, 'w', 20, True)
        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 9, 'w')
        # create subtitle : (text, justify, font_size, bg, fg, row, sticky)
        self.model.create_subtitle(" Nouvel utilisateur ", 'LEFT',
                                   ("Arial", 20), 'white', 'black', 10, 'w')
        # create button : (bd, text, font_size, bg, fg, command, row,
        #                       sticky, pady, underline)
        self.model.create_button(2, " Créer un compte ", ("Arial", 20),
                                 '#ADD0EC', "white", self.create_account(),
                                 11, 'w', 20, False)

    def login(self):
        pass

    def forgotten_password(self):
        pass

    def create_account(self):
        pass
