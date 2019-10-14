class Category:
    """..."""

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'category' table with its iD, name and
        associated number

                Args:
                    cnx : connect mysql database
                    cursor : object MySQLCursor
                """
        self.cnx = cnx
        self.cursor = cursor
        self.category_id = None
        self.name = None

    def create_category(self, name_cat):
        """This feature allows you to create a line in the category table"""

        # 1- Create a line in the food table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        # INSERT INTO `category` (`id`, `name`) VALUES (NULL, '')
        add_category = ("INSERT INTO category (name) "
                        "VALUES (%s)")
        # 1.2- Storage data in a variable
        data_category = (name_cat,)
        # 1.3- Insert new category
        self.cursor.execute(add_category, data_category)
        self.category_id = self.cursor.lastrowid
        # 1.4- Make sure data is committed
        self.cnx.commit()

    def get_id(self, name_cat):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM category "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_cat,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.category_id = row[0]

    def search_if_category_exist(self, name_cat):
        """ This function search if the category already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM category "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_cat, ))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_category(name_cat)
        else:
            self.get_id(name_cat)
            return

    def read_one_category(self):

        pass

    def read_all_category(self):
        read_all_sql = " SELECT * FROM category "
        self.cursor = self.cnx.cursor()
        self.cursor.execute(read_all_sql)

    def update_category(self):
        pass

    def delete_category(self):
        pass
