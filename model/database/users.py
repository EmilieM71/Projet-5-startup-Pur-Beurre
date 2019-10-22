class Users:

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'user' table with its iD, email,
        pseudo and password

            Args:
                cnx : connect mysql database
                cursor : object MySQLCursor
            """
        self.cnx = cnx
        self.cursor = cursor
        self.user_id = None
        self.email = None
        self.password = None
        self.pseudo = None

    def create_user(self, email, pseudo, password):
        """This feature allows you to create a line in the user table"""

        # 1- Create a line in the user table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_user = ("INSERT INTO user (e_mail, pseudo, password) "
                    "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user = (email, pseudo, password)
        # 1.3- Insert new user
        self.cursor.execute(add_user, data_user)
        self.user_id = self.cursor.lastrowid
        # 1.4- Make sure data is committed
        self.cnx.commit()
        self.send_email_create_account(email, pseudo)

    def send_email_create_account(self, email, pseudo):
        pass

    def get_id(self, pseudo, password):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM user "
                 "WHERE pseudo = %s and password = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (pseudo, password))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.user_id = row[0]
                print("id user : ", self.user_id)

    def search_if_user_exist(self, pseudo, password):
        """ This function search if the user already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM user "
                 "WHERE pseudo = %s and password = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (pseudo, password))
        rows = self.cursor.fetchall()
        if not rows:
            print("Error on pseudo or password, or account does not exist.")
            return
        else:
            self.get_id(pseudo, password)
            print("Bonjour ", pseudo)
            return
