import mysql.connector
from mysql.connector import errorcode



def query_1(word):
    '''
     Full-text search for titles of movies based that contain a specific word given as the input.
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
     Lists the movies with their average rating by all users.
    '''
    query = ("SELECT "
            "   m.title AS movie_name, "
            "   AVG(r.rating) AS average_rating "
            "FROM "
            "   matantalvi.movies m "
            "JOIN "
            "   matantalvi.ratings r ON m.movie_id = r.movie_id "
            "GROUP BY "
            "   m.title "
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


def query_4(user_id):
    '''
     given a user id, return the names of the movies he rated and the ratings for each movie .
    '''
    query = ("SELECT "
            "   m.title AS movie_name, "
            "   r.rating "
            "FROM "
            "   matantalvi.movies m "
            "JOIN "
            "   matantalvi.ratings r ON m.movie_id = r.movie_id "
            "WHERE "
            "   r.user_id = %s;"
        )
    
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query,(user_id,))
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

def query_5(movie_title):
    '''
    Given a movie name, return the runtime of the movie,
    and the average rating of the movie and the number of voters .
    '''
    query = ("SELECT "
            "   m.title AS movie_name, "
            "   m.runtime, "
            "   AVG(r.rating) AS average_rating, "
            "   COUNT(r.rating) AS num_voters "
            "FROM "
            "   matantalvi.movies m "
            "JOIN "
            "   matantalvi.ratings r ON m.movie_id = r.movie_id "
            "WHERE "
            "   m.title = %s "
            "GROUP BY "
            "   m.title, m.runtime;"
        )
    
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query,(movie_title,))
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

def query_6(year):
    '''
    Given a year, return all the movies that where released on that year and add its budget,
    order by budget 
    '''
    query = ("SELECT "
            "   m.title AS movie_name, "
            "   m.release_date, "
            "   b.budget "
            "FROM "
            "   matantalvi.movies m "
            "JOIN "
            "   matantalvi.budget b ON m.movie_id = b.movie_id "
            "WHERE "
            "   YEAR(m.release_date) = %s "
            "ORDER BY "
            "   b.budget DESC;"
        )
    
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()
        cursor.execute(query,(year,))
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

def query_7():
    '''
    returns the maximal budget with the corresponding movie of each production company.
    '''
    
    query = ("SELECT "
            "   b.prod_company, "
            "   m.title, "
            "   b.budget "
            "FROM "
            "   matantalvi.budget b "
            "JOIN "
            "   matantalvi.movies m ON b.movie_id = m.movie_id "
            "JOIN "
            "   (SELECT "
            "       prod_company, "
            "       MAX(budget) AS max_budget "
            "    FROM "
            "       matantalvi.budget "
            "    GROUP BY "
            "       prod_company) AS max_budgets "
            "ON "
            "   b.prod_company = max_budgets.prod_company "
            "   AND b.budget = max_budgets.max_budget "
            "ORDER BY "
            "   b.budget DESC;"
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
