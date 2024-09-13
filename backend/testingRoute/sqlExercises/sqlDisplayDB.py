# import os
import sqlite3 as sql

# DataType : -> NULL (not exist), INTEGER(wholeNum), REAL(decimal), TEXT(string), BLOB(file)
conn = sql.connect("members.db")  # Connect to Database
curs = conn.cursor()  # Create a Cursor to command or select

# Query the DataBase - Looking into DataBase
curs.execute("SELECT * FROM members")

# Display the Data from the Table

# curs.fetchone() # One row of the Table
# curs.fetchmany(3) # Multi-row (n row) of the Table
# curs.fetchall() # All row in the Table

table_list = curs.fetchall()
for item in table_list:
    # print(item[0]) # display only names (in this case)
    print(f"First Name:\t{item[0]}\nLast Name:\t{item[1]}\nEmail:\t\t{item[2]}\n")


# Terminal Message
# print("Command executed successfully...")
# print(curs.fetchall()) # display all of the data
# print(curs.fetchone()) # display one row of the data
# print(curs.fetchmany(3)) # display multi-row of the data (3 row in this case)

# Put the Data in the Table
conn.commit()

# Close connection
conn.close()
