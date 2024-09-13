import sqlite3

conn = sqlite3.connect('members.db')
cur = conn.cursor()


# Delete Record
# cur.execute("DELETE from members WHERE rowid = 7") # Deleting the Data in Row
cur.execute("DROP TABLE members") # Deleting the Data in Row



# Display
cur.execute("SELECT rowid, * FROM members")

data_list = cur.fetchall()
for item in data_list:
    print(item)


conn.commit()
conn.close()