import mysql.connector
from mysql.connector import errorcode

'''
try:
  cnx = mysql.connector.connect(user='matantalvi', password='mata10092',
                              host='localhost',
                              database='matantalvi',port= 3305)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

cnx = mysql.connector.connect(user='matantalvi', password='mata10092',
                              host='localhost',
                              database='matantalvi',port= 3305)
cnx.close()
'''
DB_Name = "movieDB"
TABLES = {}

def create_tables():
    # Creating movies table
    TABLES['movies'] = (
        "CREATE TABLE 'movies' ("
        "   'movie_id' INT NOT NULL,"
        "   'title' VARCHAR(50) NOT NULL,"
        "   'release_date' DATE,"
        "   'run_time' INT NOT NULL,"
        "   'adult_only' VARCHAR(50) NOT NULL,"
        "   PRIMARY KEY ('movie_id')"
        ") ENGINE=InnoDB")


    # Creating genres table
    TABLES['genres'] = (
        "CREATE TABLE 'genres' ("
        "   'genre_id' VARCHAR(50) NOT NULL,"
        "   'genre_name' varchar(50) NOT NULL,"
        "   PRIMARY KEY ('genre_id')"
        ") ENGINE=InnoDB")

    # Creating ratings table
    TABLES['ratings'] = (
        "CREATE TABLE 'ratings' ("
        "   'movie_id' VARCHAR(50) NOT NULL,"
        "   'user_id' varchar(50) NOT NULL,"
        "   'rating' FLOAT,"
        "   PRIMARY KEY ('user_id','movie_id'),"
        "   FOREIGN KEY ('movie_id') REFERENCES 'movies' ('movie_id')"
        ") ENGINE=InnoDB")


    # Creating budget table
    TABLES['budget'] = (
        "CREATE TABLE 'budget' ("
        "   'movie_id' INT NOT NULL,"
        "   'budget' INT NOT NULL,"
        "   PRIMARY KEY ('movie_id'),"
        "   FOREIGN KEY ('movie_id') REFERENCES 'movies' ('movie_id')"
        ") ENGINE=InnoDB")

    # Creating genre_movie table
    TABLES['genre_movie'] = (
        "CREATE TABLE 'genre_movie' ("
        "   'movie_id' INT NOT NULL,"
        "   'genre_id' INT NOT NULL,"
        "   PRIMARY KEY ('movie_id','genre_id),"
        "   FOREIGN KEY ('movie_id') REFERENCES 'movies' ('movie_id'),"
        "   FOREIGN KEY ('genre_id') REFERENCES 'genres' ('genre_id')"
        ") ENGINE=InnoDB")

