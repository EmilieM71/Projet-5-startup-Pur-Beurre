from model.database.manage_db import CreateDatabase


class Category:
    """..."""

    def __init__(self, category_id, name, number, db):
        """Class that characterizes the 'category' table with its iD, name and
        associated number

                Args:
                    category_id (integer): unique identifier

                    name [String] : is the name of the category

                    number (integer) : is the number associated with the
                        category (and that allows the user to choose the
                        desired category)
                    db : database
                """
        self.id = category_id
        self.name = name
        self.number = number
        self.db = db

    def create_category(self):
        create_sql = "INSERT INTO Category (name, number)" \
                     "VALUES (NULL , self.name, 'self.number');"

        self.cursor = self.cnx.cursor(create_sql)

    def read_one_category(self):
        pass

    def read_all_category(self):
        pass

    def update_category(self):
        pass

    def delete_category(self):
        pass
