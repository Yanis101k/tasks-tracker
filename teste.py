import mysql.connector

class DatabaseConnection:
    @staticmethod
    def connect():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='tasks_tracker_admin',
                password='qs%|9k)°@WhL^N^3:!§Ab',
                database='tasks_tracker',
                ssl_disabled=True
            )
            print("✅ Connected using mysql-connector-python")
            return connection
        except mysql.connector.Error as e:
            print(f"❌ Connection error: {e}")
            return None
        
DatabaseConnection.connect()