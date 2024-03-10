import mysql.connector
from mysql.connector import errorcode



def query_1(word):
    query = ("SELECT * FROM movies "
            "WHERE title LIKE CONCAT(%s, '%')")
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query, (word))
        cnx.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()

def query_2(word):
    query = ("SELECT * FROM movies "
            "WHERE title LIKE CONCAT(%s, '%')")
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query, (word))
        cnx.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()