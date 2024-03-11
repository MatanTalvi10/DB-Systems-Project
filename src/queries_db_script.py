import mysql.connector
from mysql.connector import errorcode



def query_1(word):
    '''
     Full-text search for titles of movies based on a specific word given as the input.
    '''
    query = ("SELECT * FROM movies " 
            "WHERE MATCH(title) AGAINST(%s IN NATURAL LANGUAGE MODE)")
    
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query,(word,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cnx.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()

def query_2():
    '''
     Counts the number of movies in each genre according to predetermined buckets of budget.
    '''
    query = ("SELECT "
            "   g.genre_name, "
            "   CASE "
            "       WHEN b.budget <= 1000000 THEN 'Low Budget' "
            "       WHEN b.budget <= 10000000 THEN 'Medium Budget' "
            "       ELSE 'High Budget' "
            "   END AS budget_bucket, "
            "   COUNT(*) AS movie_count "
            "FROM "
            "   movies m "
            "JOIN "
            "   budget b ON m.movie_id = b.movie_id "
            "JOIN "
            "   genre_movie gm ON m.movie_id = gm.movie_id "
            "JOIN "
            "   genres g ON gm.genre_id = g.genre_id "
            "GROUP BY "
            "   g.genre_name, budget_bucket;"
)
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cnx.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()

def query_3():
    '''
     Full-text search for titles of movies based on a specific word given as the input.
    '''
    query = ("SELECT "
        "   m.title AS movie_name, "
        "   g.genre_name, "
        "   AVG(r.rating) AS average_rating "
        "FROM "
        "   matantalvi.movies m "
        "JOIN "
        "   matantalvi.ratings r ON m.movie_id = r.movie_id "
        "JOIN "
        "   matantalvi.genre_movie gm ON m.movie_id = gm.movie_id "
        "JOIN "
        "   matantalvi.genres g ON gm.genre_id = g.genre_id "
        "GROUP BY "
        "   m.title, g.genre_name "
        "ORDER BY "
        "   m.title;"
    )
    
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cnx.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()
