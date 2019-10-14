class Food:

    def __init__(self, cnx, cursor):
        self.cnx = cnx
        self.cursor = cursor
        self.id = None
        self.name = None
        self.nutriscore = None
        self.url = None
        self.presence_food = False

    def create(self, name_food, nutriscore_food, url_food):
        """This feature allows you to create a line in the food table and
        returns the id
        :param name_food: str
        :param nutriscore_food: str
        :param url_food: str
        """
        self.cursor = self.cnx.cursor()
        # 1- Create a line in the food table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food = ("INSERT INTO food (name, nutriscore, url) "
                    "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_food = (name_food, nutriscore_food, url_food)

        # 1.3- Insert new category
        self.cursor.execute(add_food, data_food)

        self.id = self.cursor.lastrowid

        self.cnx.commit()

    def search_if_data(self):

        query = ("SELECT  id, name FROM food "
                 "WHERE id = 1")

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        if not rows:
            print("There is no data in database")
            return self.presence_food
        else:
            print("There is data in database")
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
                self.id = row[0]

    def search_if_food_exist(self, name_food, nutriscore_food, url_food):
        """ This function search if the food already exists in the database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT name FROM food "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_food, ))
        rows = self.cursor.fetchall()
        if not rows:
            self.create(name_food, nutriscore_food, url_food)
        else:
            self.get_id(name_food)
            return
