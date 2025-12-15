import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

c.execute("""
    INSERT INTO customers VALUES (
               'Mary',
               'Brown',
               'mary@codemy.com'
               )""")

print("Command executed succesfully!...")
conn.commit()
conn.close()