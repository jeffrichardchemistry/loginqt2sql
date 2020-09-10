import sqlite3
import os

ABSOLUT_PATH_table = os.path.dirname(os.path.realpath(__file__))+'/register.db'

connection = sqlite3.connect(ABSOLUT_PATH_table)
cursor = connection.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registers (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        User TEXT NOT NULL,
        Password TEXT NOT NULL,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL             
    );    
    """)

try:
    create_table()
    print('Connected to database.')
except:
    print('Error connecting to database')
    
