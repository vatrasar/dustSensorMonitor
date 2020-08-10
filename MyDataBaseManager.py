import sqlite3


class MyDataBaseManager:

    def __init__(self,path_to_db:str) -> None:
        super().__init__()
        self.sql_add_row=''' INSERT INTO dust_values(dust_density_value,test_date)
                    VALUES(?,?) '''
        self.sql_create_table=""" CREATE TABLE IF NOT EXISTS dust_values (
                                        id integer PRIMARY KEY,
                                        dust_density_value REAL NOT NULL,
                                        test_date INTEGER 
                                    ); """
        self.create_table(self.sql_create_table,path_to_db)

    def add_record(self,db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)

            conn.cursor().execute(self.sql_add_row, (23.2, 10000))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def create_table(self,create_table_sql: str, db_file_path: str):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            conn = None
            try:
                conn = sqlite3.connect(db_file_path)
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

    def get_all_records(self,db_file_path):

        try:
            conn = None
            try:
                conn = sqlite3.connect(db_file_path)
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