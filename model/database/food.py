class Food:

    def __init__(self, cnx, cursor):
        self.cnx = cnx
        self.cursor = cursor
        self.id_food = None
        self.name = None
        self.nutriscore = None
        self.url = None
        self.last_modified = None
        self.text_presence_data = None
        self.presence_food = False

    def create(self, id_food, name_food, nutriscore_food, url_food, last_modified):
        """This feature allows you to create a line in the food table and
        returns the code
        :param id_food: int
        :param name_food: str
        :param nutriscore_food: str
        :param url_food: str
        :param last_modified: date
        """
        self.cursor = self.cnx.cursor()
        # 1- Create a line in the food table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food = ("INSERT INTO food "
                    "(id, name, nutriscore, url, last_modified) "
                    "VALUES (%s, %s, %s, %s, %s)")
        # 1.2- Storage data in a variable
        data_food = (id_food, name_food, nutriscore_food, url_food,
                     last_modified)
        print("data food : id : ", id, "name food : ", name_food)

        # 1.3- Insert new category
        self.cursor.execute(add_food, data_food)

        self.id = self.cursor.lastrowid

        self.cnx.commit()

    def search_if_data(self):

        query = "SELECT id FROM food "

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        if not rows:
            # Graphical interface with Tkinter
            self.text_presence_data = "There is no data in database"
            # Mode console
            # print("There is no data in database")
            return self.presence_food
        else:
            # Graphical interface with Tkinter
            self.text_presence_data = "There is data in database"
            # Mode console
            # print("There is data in database")
            self.presence_food = True
            return self.presence_food

    def get_id(self, name_food):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM food "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_food,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.id_food = row[0]

    def search_if_food_exist(self, code, name_food, nutriscore_food,
                             url_food, last_modified):
        """ This function search if the food already exists in the database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT name FROM food "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (code, ))
        rows = self.cursor.fetchall()
        if not rows:
            self.create(code, name_food, nutriscore_food, url_food,
                        last_modified)
        else:
            self.get_id(name_food)
            return
