import mysql.connector
import requests
import MySQLdb as mdb
from mysql.connector import errorcode
import pandas as pd
import csv
import create_db_script



def main():
    create_db_script.create_tables()
    read_and_insert('budget',add_budget)
    read_and_insert('genre_movie',add_genre_movie)
    read_and_insert('genres',add_genres)
    read_and_insert('movies',add_movies)
    read_and_insert('ratings',add_ratings)









cnx = mysql.connector.connect(user='matantalvi', password='mata10092',
                              host='localhost',
                              database='matantalvi',port= 3305)

cursor = cnx.cursor()

add_movies = ("INSERT INTO movies "
               "(movie_id,title,release_date,runtime,adult_only) "
               "VALUES (%s, %s, %s, %s, %s)")

add_budget = ("INSERT INTO budget "
               "(movie_id,budget) "
               "VALUES (%s, %s)")

add_genre_movie = ("INSERT INTO genre_movies "
               "(movie_id,genres) "
               "VALUES (%s, %s)")

add_genres = ("INSERT INTO genres "
               "(genre_id,genre_name) "
               "VALUES (%s, %s)")

add_ratings = ("INSERT INTO ratings "
               "(user_id,movie_id,rating) "
               "VALUES (%s, %s, %s)")

def read_and_insert(table_name,insert_statement):
    a = 'src\\CSV files\\'
    c = '.csv'
    path = a + table_name + c
    with open(path, mode='r') as csv_data:
        reader = csv.reader(csv_data, delimiter=';')
        csv_data_list = list(reader)
        for row in csv_data_list:
            cursor.execute(insert_statement, row)
    cnx.commit()
    cursor.close()
    cnx.close()




if __name__ == "__main__":
    main()
