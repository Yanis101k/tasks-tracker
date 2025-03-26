#backend/core/database_connection
import pymysql ; 


class DatabaseConnection:

    """
    Static utility class for connecting to the MySQL database using PyMySQL.
    All methods are static — no object instantiation required.
    """

    # static database credentials ( centralized configuration )

    HOST = '127.0.0.1'
    USER = 'tasks_tracker_admin'
    PASSWORD = 'qs%|9k)°@WhL^N^3:!§Ab'
    DATABASE = 'tasks_tracker'

    @staticmethod 
    def connect() : 
        """

         Establish and return a MySql connection 
         Returns : 
               pymysql.Connection or None if failed 
        
        """
        print("Connecting with:")
        print("  Host:", DatabaseConnection.HOST)
        print("  User:", DatabaseConnection.USER)
        print("  User:", DatabaseConnection.PASSWORD)
        print("  Database:", DatabaseConnection.DATABASE)
        try : 
            connection = pymysql.connect(
                host=DatabaseConnection.HOST,
                user=DatabaseConnection.USER,
                password=DatabaseConnection.PASSWORD,
                database=DatabaseConnection.DATABASE, 
                port=3306,
                unix_socket=None,
                cursorclass=pymysql.cursors.DictCursor 
            )
            print(" Connected to the MySql database.")
        except pymysql.MySQLError as e : 
             print(" Full connection error:")
             print(e.args)
    
    @staticmethod
    def close( connection , cursor=None ) : 
        """
        Closes the cursor and connection (if provided).

        """

        if cursor : 
            cursor.close()
        if connection:
            connection.close()
            print(" Connection closed.")
DatabaseConnection.connect() ; 
