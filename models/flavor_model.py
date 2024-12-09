from models.database import get_db_connection

def get_all_flavors():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM flavors")
    flavors = cursor.fetchall()
    connection.close()  
    return flavors

def get_flavors_by_allergens(selected_allergens):
   
    connection = get_db_connection()
    cursor = connection.cursor()

   
    query = '''
        SELECT f.*
        FROM flavors f
        JOIN flavor_allergens fa ON f.id = fa.flavor_id
        JOIN allergens a ON fa.allergen_id = a.id
        WHERE a.name IN ({})
    '''.format(', '.join('?' for _ in selected_allergens))

    cursor.execute(query, selected_allergens)
    flavors = cursor.fetchall()
    connection.close()
    return flavors
