import sqlite3


class MyDataBaseManager:

    def __init__(self,path_to_db:str) -> None:
        super().__init__()
        self.path_to_db=path_to_db
        self.sql_add_row=''' INSERT INTO dust_values(dust_density_value,test_date)
                    VALUES(?,?) '''
        self.sql_create_table=""" CREATE TABLE IF NOT EXISTS dust_values (
                                        id integer PRIMARY KEY,
                                        dust_density_value REAL NOT NULL,
                                        test_date INTEGER 
                                    ); """
        self.create_table(self.sql_create_table)

    def add_record(self,dust_value:float,time:int):
        conn = None
        try:
            conn = sqlite3.connect(self.path_to_db)


            conn.cursor().execute(self.sql_add_row, (dust_value, time))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def create_table(self,create_table_sql: str):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            conn = None
            try:
                conn = sqlite3.connect(self.path_to_db)
                print(sqlite3.version)

                c = conn.cursor()
                c.execute(create_table_sql)
                conn.commit()
            except sqlite3.Error as e:
                print(e)
            finally:
                if conn:
                    conn.close()

        except sqlite3.Error as e:
            print(e)

    def get_all_records(self):

        try:
            conn = None
            try:
                conn = sqlite3.connect(self.path_to_db)
                print(sqlite3.version)

                cur = conn.cursor()
                cur.execute("SELECT * FROM dust_values")
                rows = cur.fetchall()
                return rows
            except sqlite3.Error as e:
                print(e)
            finally:
                if conn:
                    conn.close()

        except sqlite3.Error as e:
            print(e)