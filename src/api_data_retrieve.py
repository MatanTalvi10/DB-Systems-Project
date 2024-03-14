import mysql.connector
import MySQLdb as mdb
from mysql.connector import errorcode
import pandas as pd
import csv
import create_db_script
from datetime import datetime 
import queries_db_script as qds



def main():
    create_db_script.main()
    read_and_insert('movies',add_movies)
    read_and_insert('budget',add_budget)
    read_and_insert('genres',add_genres)
    read_and_insert('genre_movie',add_genre_movie)
    read_and_insert('ratings',add_ratings)
    

add_movies = ("INSERT INTO movies(movie_id,title,release_date,runtime,adult_only) "
               "VALUES (%s, %s, %s, %s, %s)")

add_budget = ("INSERT INTO budget "
               "(movie_id,budget) "
               "VALUES (%s, %s)")

add_genre_movie = ("INSERT INTO genre_movie "
               "(movie_id,genre_id) "
               "VALUES (%s, %s)")

add_genres = ("INSERT INTO genres "
               "(genre_id,genre_name) "
               "VALUES (%s, %s)")

add_ratings = ("INSERT INTO ratings "
               "(user_id,movie_id,rating) "
               "VALUES (%s, %s, %s)")


def read_and_insert(table_name, insert_statement):
    try:
        cnx = mysql.connector.connect(
            user='matantalvi', password='mata10092',
            host='localhost', database='matantalvi', port=3305
        )
        cursor = cnx.cursor()

        a = 'src\\CSV files\\'
        c = '.csv'
        path = a + table_name + c

        with open(path, mode='r', encoding='utf-8') as csv_data:
            reader = csv.reader(csv_data, delimiter=',')
            next(reader)
            for row in reader:
                if table_name == 'movies':
                    row[2] = convert_date(row[2])
                cursor.execute(insert_statement, tuple(row))

        cnx.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()

def convert_date(date_str):
    # Convert date from 'DD/MM/YYYY' to 'YYYY-MM-DD'
    return datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d') 

if __name__ == "__main__":
    main()

