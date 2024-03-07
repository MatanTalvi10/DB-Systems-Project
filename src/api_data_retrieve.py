import mysql.connector
import requests
import MySQLdb as mdb
from mysql.connector import errorcode
import pandas as pd

# Loading csv content
df_budget = pd.read_csv("src\\CSV files\\budget.csv")
df_genre_movie = pd.read_csv("src\\CSV files\\genre_movie.csv")
df_genres = pd.read_csv("src\\CSV files\\genres.csv")
df_movies = pd.read_csv("src\\CSV files\\movies.csv")
df_ratings = pd.read_csv("src\\CSV files\\ratings.csv")


add_movies = ("INSERT INTO movies "
               "(movie_id,title,release_date,runtime,adult_only) "
               "VALUES (%s, %s, %s, %s, %s)")

add_budget = ("INSERT INTO budget "
               "(movie_id,budget) "
               "VALUES (%s, %s)")

add_genre_movies = ("INSERT INTO genre_movies "
               "(movie_id,genres) "
               "VALUES (%s, %s)")

add_genres = ("INSERT INTO genres "
               "(genre_id,genre_name) "
               "VALUES (%s, %s)")

add_ratings = ("INSERT INTO ratings "
               "(user_id,movie_id,rating) "
               "VALUES (%s, %s, %s)")





