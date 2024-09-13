import sqlite3 

conn = sqlite3.connect('members.db')
cur = conn.cursor()

# cur.execute("SELECT rowid, * FROM members WHERE last_name = 'Dwin' ") # Display specific Data
# cur.execute("SELECT rowid, * FROM members WHERE last_name LIKE 'Will%' ") # Display same Data
# cur.execute("SELECT rowid, * FROM members WHERE email LIKE '%adam.com' ") # Display same Data
# cur.execute("SELECT rowid, * FROM members WHERE email LIKE '%adam.com' OR rowid = 4 ") # Display the Data by rowid (or) by email (either can be True)
# cur.execute("SELECT rowid, * FROM members WHERE email LIKE '%adam.com' AND rowid = 2") # Display same Data by rowid (and) by email (both must be the same)
# cur.execute("SELECT rowid, * FROM members LMIT 2") # Display Limited Data from Members Table
# cur.execute("SELECT rowid, * FROM members ORDER BY rowid LMIT 2") # Display Limited Data from Members Table
# cur.execute("SELECT rowid, * FROM members ORDER BY rowid DESC LMIT 2") # Display Limited Data from Members Table in (DESC - 10 to 1) order [In this case]
# cur.execute("SELECT rowid, * FROM members ORDER BY rowid DESC") # Display all Data from Members Table by in (DESC) order or in (ASC (Default)) order
cur.execute("SELECT rowid, * FROM members") # Display all Data from Members Table

items = cur.fetchall()

for item in items:
    print(item)



conn.commit()
conn.close()