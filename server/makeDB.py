import sqlite3
from contextlib import closing

def create_table():
    DB_NAME = "salesioFes.db"

    with closing(sqlite3.connect(DB_NAME)) as conn:
        c = conn.cursor()

        create_table = '''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        className TEXT NOT NULL, name TEXT NOT NULL, price INT NOT NULL)'''

        c.execute(create_table)

        create_table = '''CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        className TEXT NOT NULL, productID INT NOT NULL, amount INT NOT NULL)'''

        c.execute(create_table)