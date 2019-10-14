from tkinter import *
from tkinter import font


class ViewWelcomeWindow:
    """"""

    def __init__(self):
        # Create window
        self.window = Tk()
        # personalization of the window
        self.window.title("Pur Beurre ")
        self.window.geometry("480x600")
        self.window.minsize(480, 480)
        # self.window.iconbitmap("documentation/Image/OpenFoodFacts.ico")
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
        self.create_line(1)
        self.create_subtitle(" Information : ", 2)
        self.create_line(3)
        text_info = """ To use the app you need to have 
        - to install MySQL version 8, 
        - create user : name :'student_OC', 
                                host: 'localhost', 
                                password : '123abc' """
        self.create_text(text_info, 4, 'white')
        text_create_user = " To create a user, log in to MySQL and enter : "
        self.create_text(text_create_user, 5, 'white')
        create_user_sql_line1 = " CREATE USER IF NOT EXISTS 'student_OC'@'localhost' IDENTIFIED BY '123abc'; "
        self.create_text(create_user_sql_line1, 6, 'gray')
        create_user_sql_line2 = " GRANT ALL PRIVILEGES ON elevage.* TO 'student'@'localhost'; "
        self.create_text(create_user_sql_line2, 7, 'gray')
        self.create_line(8)
        self.create_subtitle(" Click the button on your choice : ", 9)
        self.create_line(10)
        text_choice_1 = " launch the app "
        self.create_button(2, text_choice_1, '#ADD0EC', "white", 11,
                           False, self.launch_the_app())
        text_choice_2 = "Enter 2 to leave"
        self.create_button(2, text_choice_2, '#ADD0EC', "white", 12,
                           False, self.leave())

    def create_title(self):
        label_title = Label(self.frame, text=" WELCOME ",
                            font=("Arial", 40), bg='white', fg='#ADD0EC')
        label_title.grid(row=0, sticky='w')

    def create_subtitle(self, text, row):
        label_subtitle = Label(self.frame, text=text, justify=LEFT,
                               font=("Arial", 15), bg='white', fg='black')
        label_subtitle.grid(row=row, sticky='w')

    def create_line(self, row):
        canvas = Canvas(self.frame, bd=0, highlightthickness=0,
                        background="white", height=20)
        canvas.create_line((10, 10), (370, 10), fill='#ADD0EC', width=2)
        canvas.grid(row=row, sticky='w')

    def create_text(self, text, text_row, bg):
        label = Label(self.frame, text=text, font=("Arial", 8),
                      wraplength=450, bg=bg, fg='black', justify=LEFT)
        label.grid(row=text_row, sticky='w')

    def create_button(self, bd, text, bg, fg, row, underline,
                      command):
        button = Button(self.frame, bd=bd, text=text,
                        font=("Arial", 15), bg=bg, fg=fg,
                        command=command)
        button.grid(row=row, sticky='w', pady=20)
        f = font.Font(button, button.cget("font"))
        f.configure(underline=underline)
        button.configure(font=f)

    def launch_the_app(self):
        pass

    def leave(self):
        pass


    # afficher


home_window = ViewWelcomeWindow()
home_window.window.mainloop()
pass
