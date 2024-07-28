import os
import psycopg2

private_vars = os.environ
DB_HOST: str = private_vars["DB_HOST"]
DB_PORT: str = private_vars["DB_PORT"]
DB_NAME: str = private_vars["DB_NAME"]
DB_USER: str = private_vars["DB_USER"]
DB_PASSWORD: str = private_vars["DB_PASSWORD"]


class DBConnection:
    """
    A class to manage database connections and operations.

    Attributes:
        db_host (str): The database host.
        db_port (str): The database port.
        db_name (str): The database name.
        db_user (str): The database user.
        db_password (str): The database user's password.

    Methods:
        get_connection() -> psycopg2.connect:
            Establishes and returns a new database connection with autocommit enabled.
        read_gigabuse_words() -> list:
            Reads and returns words from the 'gigabuse_words' table.
    """
    def __init__(self):
        """
        Initializes DBConnection with database connection parameters.
        """
        self.db_host: str = DB_HOST
        self.db_port: str = DB_PORT
        self.db_name: str = DB_NAME
        self.db_user: str = DB_USER
        self.db_password: str = DB_PASSWORD


    def get_connection(self) -> psycopg2.connect:
        """
        Establishes and returns a new database connection with autocommit enabled.

        Returns:
            psycopg2.connect: A new database connection.
        """
        connection: psycopg2.connect = psycopg2.connect(
            host=self.db_host, port=self.db_port,
            database=self.db_name, user=self.db_user,
            password=self.db_password, sslmode="disable"
        )
        connection.autocommit = True
        return connection


    def read_gigabuse_words(self) -> list:
        """
        Reads and returns words from the 'gigabuse_words' table.

        Returns:
            list: A list containing two elements:
                  1. A list of tuples containing the words from the 'gigabuse_words' table.
                  2. A list of column names from the 'gigabuse_words' table.

        Raises:
            Exception: If an error occurs while querying the database.
        """
        connection: psycopg2.connect = None
        try:
            connection = self.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT gw.word FROM gigabuse_words AS gw;")
                column_names: list[str] = [desc[0] for desc in cursor.description]
                res: tuple = cursor.fetchall()
                return [res, column_names]

        except Exception as _ex:
            print(f"[DBConnection->read_gigabuse_words]. Can't process query. Error :: {_ex}")
            return [(), ()]

        finally:
            if connection is not None:
                connection.close()
