import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

c.execute("SELECT * FROM customers")
# print(c.fetchone()[1])
# c.fetchmany(3)
# print(c.fetchall())

items = c.fetchall()



conn.commit()
conn.close()