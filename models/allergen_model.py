
from models.database import get_db_connection

def add_allergen(name, user_defined=False):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO allergens (name, is_user_defined) VALUES (?, ?)", (name, user_defined))
    connection.commit()
    connection.close()

def remove_user_allergen(allergen_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM allergens WHERE id = ? AND is_user_defined = 1", (allergen_id,))
    connection.commit()
    connection.close()

def get_all_allergens():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM allergens")
    allergens = cursor.fetchall()
    connection.close()
    return allergens
