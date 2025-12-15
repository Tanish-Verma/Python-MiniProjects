import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

customers = [
    ("henry","sandwhich","henry@sandwhich"),
    ("john","doe","john@doe"),
    ("mon","day","mon@day")]

c.executemany("INSERT INTO customers VALUES (?,?,?)",customers)

print("Command executed succesfully!...")
conn.commit()
conn.close()