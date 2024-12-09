from models.database import get_db_connection

def add_to_cart(flavor_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO cart (flavor_id) VALUES (?)", (flavor_id,))
    connection.commit()
    connection.close()

def get_cart_items():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT f.name AS flavor_name
        FROM cart c
        JOIN flavors f ON c.flavor_id = f.id
    """)
    items = cursor.fetchall()
    connection.close()
    return items

def clear_cart():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cart")
    connection.commit()
    connection.close()
