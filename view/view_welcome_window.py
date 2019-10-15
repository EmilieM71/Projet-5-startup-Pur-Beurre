from model.view.model import ViewModel


class ViewWelcomeWindow:
    """"""

    def __init__(self):
        self.model = ViewModel()

        # creating window components
        self.create_widgets()

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
        # create subtitle : (text, justify, font_size, bg, fg, row, sticky)
        self.model.create_subtitle(" Information : ", 'LEFT', ("Arial", 15),
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
        # create text : (text, font_size, wraplength, bg, fg, justify,
        # row, sticky)
        self.model.create_text(text_info, ("Arial", 8), 450, 'white', 'black',
                               'LEFT', 4, 'w')

        text_create_user = " To create a user, log in to MySQL and enter : "
        # create text: (text, font_size, wraplength, bg, fg, justify,
        # row, sticky)
        self.model.create_text(text_create_user, ("Arial", 8), 450, 'white',
                               'black', 'LEFT', 5, 'w')

        create_user_sql_line1 = (" CREATE USER IF NOT EXISTS "
                                 "'student_OC'@'localhost' "
                                 "IDENTIFIED BY '123abc'; ")

        # create text: (text, font_size, wraplength, bg, fg, justify,
        # row, sticky)
        self.model.create_text(create_user_sql_line1, ("Arial", 8), 450,
                               'gray', 'black', 'LEFT', 6, 'w')

        create_user_sql_line2 = (" GRANT ALL PRIVILEGES ON elevage.* "
                                 "TO 'student'@'localhost'; ")

        # create text: (text, font_size, wraplength, bg, fg, justify,
        # row, sticky)
        self.model.create_text(create_user_sql_line2, ("Arial", 8), 450,
                               'gray', 'black', 'LEFT', 7, 'w')

        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 8, 'w')

        # create subtitle : (text, justify, font_size, bg, fg, row, sticky)
        self.model.create_subtitle(" Click the button on your choice : ",
                                   'LEFT', ("Arial", 15), 'white', 'black',
                                   9, 'w')

        # create line : (bd, highlightthickness, bg, height,
        #                     x0, y0, x1, y1, fill, width, row, sticky)
        self.model.create_line(0, 0, "white", 20, 10, 10, 370, 10, '#ADD0EC',
                               2, 10, 'w')

        text_choice_1 = " launch the app "
        # create button : (bd, text, font_size, bg, fg, command, row,
        #                       sticky, pady, underline)
        self.model.create_button(2, text_choice_1, ("Arial", 20), '#ADD0EC',
                                 "white", self.launch_the_app(), 11, 'w', 20,
                                 False)

        text_choice_2 = "Enter 2 to leave"
        # create button : (bd, text, font_size, bg, fg, command, row,
        #                       sticky, pady, underline)
        self.model.create_button(2, text_choice_2, ("Arial", 20), '#ADD0EC',
                                 "white", self.leave(), 12, 'w', 20,
                                 False)

    def launch_the_app(self):
        pass

    def leave(self):
        pass
