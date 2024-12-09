
import sqlite3

def get_db_connection():
    connection = sqlite3.connect('ice_cream.db')
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS flavors (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            is_seasonal BOOLEAN NOT NULL,
            ingredients TEXT NOT NULL  -- New column to store ingredients/allergens
        );
        CREATE TABLE IF NOT EXISTS allergens (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY,
            flavor_id INTEGER,
            FOREIGN KEY (flavor_id) REFERENCES flavors(id)
        );
    ''')
    connection.commit()
    connection.close()
