from tkinter import *
from tkinter import font


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

        # creating window components
        self.create_widgets()

        # display
        self.frame.pack(expand=YES)

    def create_widgets(self):
        """

        :rtype:
        """
        self.create_title()
        self.create_subtitle(" Se connecter ", 1)
        self.create_line(2)
        self.create_label_entry(" Pseudo ", 3)
        self.create_label_entry(" Password ", 5)
        self.create_button(2, " se connecter ", 20, '#ADD0EC', "white", 7,
                           False, self.login())
        self.create_button(0, " Mot de passe oublié ", 10, "white", 'blue',
                           8, True, self.forgotten_password())
        self.create_line(9)
        self.create_subtitle(" Nouvel utilisateur ", 10)
        self.create_button(2, " Créer un compte ", 20, '#ADD0EC', "white", 11,
                           False, self.create_account())

    def create_title(self):
        label_title = Label(self.frame, text=" Bienvenue ",
                            font=("Arial", 40), bg='white', fg='#ADD0EC')
        label_title.grid(row=0, sticky='w')

    def create_subtitle(self, text, row):
        label_subtitle = Label(self.frame, text=text, justify=LEFT,
                               font=("Arial", 20), bg='white', fg='black')
        label_subtitle.grid(row=row, sticky='w')

    def create_line(self, row):
        canvas = Canvas(self.frame, bd=0, highlightthickness=0,
                        background="white", height=20)
        canvas.create_line((10, 10), (370, 10), fill='#ADD0EC', width=2)
        canvas.grid(row=row, sticky='w')

    def create_label_entry(self, label_text, label_row):
        label = Label(self.frame, text=label_text, font=("Arial", 15),
                      bg='white', fg='black')
        label.grid(row=label_row, column=0, sticky='w')
        entry = Entry(self.frame, font=("Arial", 20), bg='white', fg='black')
        entry.grid(row=(label_row + 1), sticky='w')

    def create_button(self, bd, text, font_size, bg, fg, row, underline,
                      command):
        button = Button(self.frame, bd=bd, text=text,
                        font=("Arial", font_size), bg=bg, fg=fg,
                        command=command)
        button.grid(row=row, sticky='w', pady=20)
        f = font.Font(button, button.cget("font"))
        f.configure(underline=underline)
        button.configure(font=f)

    def login(self):
        pass

    def forgotten_password(self):
        pass

    def create_account(self):
        pass


# afficher
home_window = ViewHomeConnect()
home_window.window.mainloop()
