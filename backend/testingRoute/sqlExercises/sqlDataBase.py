import sqlite3


# Query the DATABASE and Return ALL Records
def show_allData():
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    cur.execute("SELECT rowid, * FROM members")
    data_list = cur.fetchall()
    for item in data_list:
        print(item)

    conn.commit()
    conn.close()


# Add a New Record to the Table
def add_record(first, last, email):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO members VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()


# Add Many Records to the Table
def add_manyRecord(list):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    cur.executemany("INSERT INTO members VALUES (?,?,?)", (list))

    conn.commit()
    conn.close()


# Delete Record from Table
def delete_record(row_id):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    # cur.execute("DELETE from members WHERE rowid = ?", (row_id,)) # The comma is necessary to define a single-element tuple in Python.
    cur.execute("DELETE from members WHERE rowid = (?)", row_id)

    conn.commit()
    conn.close()


# LookUp the Data with WHERE from Table
def email_lookUp(email):
    conn = sqlite3.connect("members.db")
    cur = conn.cursor()

    # cur.execute("SELECT * from members WHERE email LIKE ?", (f'%{email}%',)) # Finding data using LIKE with f stringFormat
    cur.execute("SELECT * from members WHERE email LIKE '"+email+"'") # Finding data with Full Length
    # cur.execute(
    #     "SELECT * from members WHERE email = ?", (email,)
    # )  # Finding data using LIKE
    data_list = cur.fetchall()
    for item in data_list:
        print(item)

    conn.commit()
    conn.close()
