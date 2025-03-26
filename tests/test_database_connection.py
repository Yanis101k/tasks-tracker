import sys
import os

# This makes Python see the parent folder of /tests as part of the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.database_connection import DatabaseConnection

def test_connection():
    conn = DatabaseConnection.connect()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")  # Just to test DB is working
        users = cursor.fetchall()

        print("✅ Connected! Here are the users:")
        for user in users:
            print(user)

        DatabaseConnection.close(conn, cursor)
    else:
        print("❌ Could not connect to database.")

# Run this test when file is executed
if __name__ == "__main__":
    test_connection()
