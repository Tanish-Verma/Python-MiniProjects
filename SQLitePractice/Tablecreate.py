import sqlite3

#connect to db
conn = sqlite3.connect('customer.db')

# create a cursor
cursor = conn.cursor()

#create a table

cursor.execute("""
    CREATE TABLE customers(
        first_name text,
        last_name text,
        Email text
)""")

# There are only 5 Data types in SQLite 
'''
NULL
INTEGER
REAL
TEXT
BLOB

'''
#commit our command
conn.commit()

#close the connection
conn.close()