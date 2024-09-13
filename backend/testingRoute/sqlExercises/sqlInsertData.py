# import os
import sqlite3 as sql

# DataType : -> NULL (not exist), INTEGER(wholeNum), REAL(decimal), TEXT(string), BLOB(file)
conn = sql.connect("members.db")  # Connect to Database
curs = conn.cursor()  # Create a Cursor to command or select

# Insert Multi-Data to Table
members_list = [
    ("John", "Will", "john@will.com"),
    ("Mark", "Adam", "mark@adam.com"),
    ("Kaven", "Swift", "kaven@swift.com"),
    ("Kall", "Dwin", "kaven@swift.com"),
]
curs.executemany("INSERT INTO members VALUES (?,?,?)", members_list)

# Terminal Message
print("Data has been added to the Table successfully...")

# Put the Data in the Table
conn.commit()

# Close connection
conn.close()
