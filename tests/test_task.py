# tests/test_database_connection.py

from backend.core.database_connection import DatabaseConnection

def test_connection():
    conn = DatabaseConnection.connect()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()

        print(" Users from database:")
        for user in users:
            print(user)

        DatabaseConnection.close(conn, cursor)
    else:
        print(" Failed to connect.")

# Run the test manually
test_connection()