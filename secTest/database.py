import sqlite3


def create_dataBase():
    connet_database = sqlite3.connect("members.db")
    cursor_select = connet_database.cursor()

    table_head = """CREATE TABLE IF NOT EXISTS members (
                  username TEXT NOT NULL,
                  email TEXT PRIMARY KEY,
                  userpassword TEXT NOT NULL)
"""
    cursor_select.execute(table_head)
    connet_database.commit()
    connet_database.close()


def user_signUp(username, email, password):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO members (username, email, userpassword) VALUES (?, ?, ?)",
            (username, email, password),
        )
        conn.commit()
        print("User signed up successfully!")
    except sqlite3.IntegrityError:
        print("An account with this email already exists.")
    finally:
        conn.close()


def user_login(email, password):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM members WHERE email = ? AND userpassword = ?", (email, password)
    )
    user = cur.fetchone()

    if user:
        print(f"Welcome back, {user[0]}!")  # Greet the user by their username
    else:
        print("Invalid email or password.")

    conn.close()


def delete_info(email):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    try:
        # Delete user by email
        cur.execute("DELETE FROM members WHERE email = ?", (email,))
        conn.commit()
        print(f"Account with email '{email}' deleted successfully!")
    except sqlite3.Error as e:
        print(f"Error deleting account: {e}")
    finally:
        conn.close()


def update_userInfo(username, email, password):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    try:
        cur.execute(
            "UPDATE members SET (username, email, userpassword) VALUES (?, ?, ?)",
            (username, email, password),
        )
        conn.commit()
        print("User Info updated successfully!")
    except sqlite3.IntegrityError:
        print("An account with this email already exists.")
    finally:
        conn.close()


def show_userInfo(userpassword):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM members WHERE userpassword = ?", (userpassword,))
        info_list = cur.fetchall()
        for info in info_list:
            print(f"User Informations:\nUsername:\t{info[0]}\nEmail:\t\t{info[1]}")

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()
