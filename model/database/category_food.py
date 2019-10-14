class CategoryFood:
    """..."""

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'category_food' table with its
        id_category, id_food.

                Args:
                    cnx : connect mysql database
                """
        self.cnx = cnx
        self.cursor = cursor
        self.cat_id = None
        self.food_id = None

    def create_category_food(self, cat_id, food_id):
        """This feature allows you to create a line in the category_food
        table"""

        # 1- Create a line in the food category_food
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_category_food = ("INSERT INTO category_food (id_category, id_food)"
                             "VALUES (%s, %s)")
        # 1.2- Storage data in a variable
        data_category_food = (cat_id, food_id)
        # 1.3- Insert new category
        self.cursor.execute(add_category_food, data_category_food)
        # 1.4- Make sure data is committed
        self.cnx.commit()

    def search_if_cat_food_exist(self, cat_id, food_id):
        """ This function search if the food already exists in the database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM category_food "
                 "WHERE id_category = %s and id_food = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (cat_id, food_id))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_category_food(cat_id, food_id)
        else:
            return

    def read_one_category_food(self):
        pass

    def read_all_category_food(self):
        pass

    def update_category_food(self):
        pass

    def delete_category_food(self):
        pass
