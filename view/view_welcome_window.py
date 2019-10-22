from tkinter import *
from tkinter.messagebox import *
from model.view.model import ViewModel
from view.view_steps_windows import ViewStepsWindows


class ViewWelcomeWindow:
    """"""

    def __init__(self):

        # self.
        # create a window with title, size, minimal size and white background
        self.window = Tk()
        self.window.title(" Pur Beurre ")
        self.window.geometry("480x600")
        self.window.minsize(480, 480)
        # self.window.iconbitmap(" logo.ico ")
        self.window.config(background='white')
        # Create frame in window
        self.frame = Frame(self.window, bg='white')
        self.model = ViewModel(self.frame)
        # self.app_launch = False

        # creating window components
        self.create_widgets()

        # display
        self.frame.pack(expand=YES)

    def create_widgets(self):
        """

        :rtype:
        """
        # create title : (text, font_size, bg, fg, row, sticky)
        self.model.create_title(" WELCOME ", ("Arial", 40), 'white',
                                '#ADD0EC', 0, 'w')
        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 1, 'w')
        # create subtitle : (text, font_size, bg, fg, row, sticky)
        self.model.create_subtitle(" Information : ", ("Arial", 15),
                                   'white', 'black', 2, 'w')
        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 3, 'w')

        text_info = """ To use the app you need to have 
        - to install MySQL version 8, 
        - create user : name :'student_OC', 
                                host: 'localhost', 
                                password : '123abc' """
        # create text : (text, font_size, bg, fg, row, sticky)
        self.model.create_text(text_info, ("Arial", 8), 'white', 'black',
                               4, 'w')

        text_create_user = " To create a user, log in to MySQL and enter : "
        # create text: (text, font_size, wraplength, bg, fg, row, sticky)
        self.model.create_text(text_create_user, ("Arial", 8), 'white',
                               'black', 5, 'w')
        text_CU = """
        1 CREATE USER 'student_OC'@'localhost' IDENTIFIED BY '123abc'; 
        2 GRANT ALL PRIVILEGES ON PurBeurre.* TO 'student'@'localhost';
        """
        self.model.create_text(text_CU, ("Arial", 8), 'black', 'white', 6, 'w')

        # create_user_sql_line1 = (" CREATE USER IF NOT EXISTS "
        #                          "'student_OC'@'localhost' "
        #                          "IDENTIFIED BY '123abc'; ")
        #
        # # create text: (text, font_size, wraplength, bg, fg, row, sticky)
        # self.model.create_text(create_user_sql_line1, ("Arial", 8), 450,
        #                        'gray', 'black', 6, 'w')
        #
        # create_user_sql_line2 = (" GRANT ALL PRIVILEGES ON PurBeurre.* "
        #                          "TO 'student'@'localhost'; ")
        #
        # # create text: (text, font_size, wraplength, bg, fg, row, sticky)
        # self.model.create_text(create_user_sql_line2, ("Arial", 8), 450,
        #                        'gray', 'black', 7, 'w')
        # Create
        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 8, 'w')

        # create subtitle : (text, font_size, bg, fg, row, sticky)
        self.model.create_subtitle(" Click the button on your choice : ",
                                   ("Arial", 15), 'white', 'black', 9, 'w')

        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 10, 'w')

        text_choice_1 = "   launch the app   "
        # create button : (bd, text, font_size, bg, fg, command, row,
        #                       sticky, pady, underline)
        self.model.create_button(2, text_choice_1, ("Arial", 20), '#ADD0EC',
                                 "white", self.launch_the_app, 11, 'ns', 20,
                                 False)

        text_choice_2 = "            exit           "
        # create button : (bd, text, font_size, bg, fg, command, row,
        #                       sticky, pady, underline)
        self.model.create_button(2, text_choice_2, ("Arial", 20), '#ADD0EC',
                                 "white", self.leave, 12, 'ns', 20,
                                 False)

    # @staticmethod
    # def open_steps_window():
    #     # Opening the steps windows
    #     view_steps = ViewStepsWindows()
    #     view_steps.window.mainloop()

    def launch_the_app(self):
        # close the welcome window
        self.window.destroy()
        # Open the steps window
        view_steps_window = ViewStepsWindows()
        view_steps_window.window.mainloop()

    def leave(self):
        self.window.destroy()
