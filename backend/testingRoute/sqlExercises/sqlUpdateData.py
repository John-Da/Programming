import sqlite3

conn = sqlite3.connect("members.db")
cur = conn.cursor()


# Update Records
cur.execute(
    """
    UPDATE members SET 
    email = 'bob@will.com' WHERE
    rowid = 4
    """
)
conn.commit()


# Display the desired Data
cur.execute("SELECT rowid, * FROM members")

data_list = cur.fetchall()
for item in data_list:
    print(item)


conn.commit()
conn.close()
