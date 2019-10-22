class UserFood:

    def __init__(self, cnx, cursor):

        self.cnx = cnx
        self.cursor = cursor
        self.id_food = None
        self.id_user = None
        self.id_substitute = None

    def create_user_food(self, user_id, food_id, substitute_id):
        """This feature allows you to create a line in the user_food
        table"""

        # 1- Create a line
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_user_food = ("INSERT INTO user_food "
                         "(id_user, id_food, id_substitute)"
                         "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user_food = (user_id, food_id, substitute_id)
        # 1.3- Insert new food_store
        self.cursor.execute(add_user_food, data_user_food)
        # 1.4- Make sure data is committed
        self.cnx.commit()

    def search_if_user_food_exist(self, user_id, food_id, substitute_id):
        """ This function search if the user_food already exists in the
        database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM user_food "
                 "WHERE id_user = %s and  = %s and id_substitute = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (user_id, food_id, substitute_id))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_user_food(user_id, food_id, substitute_id)
        else:
            return


