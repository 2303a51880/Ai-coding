import sqlite3


def get_user(username):
    if not username or not isinstance(username, str):
        raise ValueError("Invalid username provided.")

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))

        result = cursor.fetchone()
        return result

    except sqlite3.Error as error:
        print("Database error occurred:", error)
        return None

    finally:
        if conn:
            conn.close()


user = input("Enter username: ").strip()

try:
    user_data = get_user(user)
    print(user_data)
except ValueError as ve:
    print("Input Error:", ve)
