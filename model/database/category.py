# from model.database.manage_db import CreateDatabase


class Category:
    """..."""

    def __init__(self, category_id, name, number, db, cursor):
        """Class that characterizes the 'category' table with its iD, name and
        associated number

                Args:
                    category_id (integer): unique identifier

                    name [String] : is the name of the category

                    number (integer) : is the number associated with the
                        category (and that allows the user to choose the
                        desired category)

                """
        self.id = category_id
        self.name = name
        self.number = number
        self.cursor = cursor
        self.cnx = None

    def create_category(self, name, number):
        add_category = ("INSERT INTO category (name, number) "
                        "VALUES (%s, %s)")

        data_category = (name, number)

        # Insert new category
        self.cursor.execute(add_category, data_category)
        cat_id = self.cursor.lastrowid

        # Make sure data is committed to the database
        self.cnx.commit()

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
