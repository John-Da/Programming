import sqlite3 as sql

# DataType : -> NULL (not exist), INTEGER(wholeNum), REAL(decimal), TEXT(string), BLOB(file)
conn = sql.connect("members.db")  # Connect to Database
curs = conn.cursor()  # Create a Cursor to command or select

# Create a Table
curs.execute(
    """CREATE TABLE members (
             first_name text,
             last_name text,
             email text
)"""
)  # by Doc String

# Terminal Message
print("Table has been created successfully...")

# Put the Data in the Table
conn.commit()

# Close connection
conn.close()
