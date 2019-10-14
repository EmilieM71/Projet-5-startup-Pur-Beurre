class Brand:
    """..."""

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'brand' table with its iD and name
                Args:
                    cnx : connect mysql database
                    cursor : object MySQLCursor
                """
        self.cnx = cnx
        self.cursor = cursor
        self.brand_id = None
        self.brand_name = None

    def create_brand(self, name_brand):
        """This feature allows you to create a line in the category table"""

        # 1- Create a line in the brand table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_brand = ("INSERT INTO brand (name) "
                     "VALUES (%s)")
        # 1.2- Storage data in a variable
        data_brand = (name_brand,)
        # 1.3- Insert new category
        self.cursor.execute(add_brand, data_brand)
        self.brand_id = self.cursor.lastrowid
        # 1.4- Make sure data is committed
        self.cnx.commit()

    def get_id(self, name_brand):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM brand "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_brand,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.brand_id = row[0]

    def search_if_brand_exist(self, name_brand):
        """ This function search if the brand already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM brand "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_brand,))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_brand(name_brand)
        else:
            self.get_id(name_brand)
            return

    def read_one_brand(self):

        pass

    def read_all_brand(self):
        read_all_sql = " SELECT * FROM brand "
        self.cursor = self.cnx.cursor()
        self.cursor.execute(read_all_sql)

    def update_brand(self):
        pass

    def delete_brand(self):
        pass
