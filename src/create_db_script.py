import mysql.connector
from mysql.connector import errorcode

def main():
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
  cnx.reconnect()
  cursor = cnx.cursor()
  
  # if you want to test our "create_db_script use this DROP loop"
  ''' 
  e = "DROP TABLE movies"
  b = "DROP TABLE budget"
  a = "DROP TABLE genre_movie"
  c = "DROP TABLE genres"
  d = "DROP TABLE ratings"
  L = [a,b,c,d,e]
  for i in L:
    cursor.execute(i)  
  '''
  DB_NAME = "movieDB"
  TABLES = {}

  # Creating movies table
  TABLES['movies'] = (
      "CREATE TABLE IF NOT EXISTS movies ("
      "   movie_id INT NOT NULL,"
      "   title VARCHAR(100) NOT NULL,"
      "   release_date DATE,"
      "   runtime INT NOT NULL,"
      "   adult_only VARCHAR(50) NOT NULL,"
      "   PRIMARY KEY (movie_id),"
      "   FULLTEXT idx1 (title)"
      ") ENGINE=InnoDB")

  # Creating genres table
  TABLES['genres'] = (
      "CREATE TABLE IF NOT EXISTS genres ("
      "   genre_id INT NOT NULL,"
      "   genre_name varchar(50) NOT NULL,"
      "   PRIMARY KEY (genre_id),"
      "   FULLTEXT idx2 (genre_name)"
      ") ENGINE=InnoDB")
  
  # Creating ratings table
  TABLES['ratings'] = (
      "CREATE TABLE IF NOT EXISTS ratings ("
      "   movie_id INT NOT NULL,"
      "   user_id INT NOT NULL,"
      "   rating FLOAT,"
      "   PRIMARY KEY (user_id,movie_id),"
      "   FOREIGN KEY (movie_id) REFERENCES movies (movie_id)"
      ") ENGINE=InnoDB")


  # Creating budget table
  TABLES['budget'] = (
      "CREATE TABLE IF NOT EXISTS budget ("
      "   movie_id INT NOT NULL,"
      "   budget INT NOT NULL,"
      "   prod_company varchar(100) NOT NULL,"
      "   PRIMARY KEY (movie_id, prod_company),"
      "   FOREIGN KEY (movie_id) REFERENCES movies (movie_id)"
      ") ENGINE=InnoDB")

# Creating genre_movie table
  TABLES['genre_movie'] = (
      "CREATE TABLE IF NOT EXISTS genre_movie ("
      "   movie_id INT NOT NULL,"
      "   genre_id INT NOT NULL,"
      "   PRIMARY KEY (movie_id, genre_id),"
      "   FOREIGN KEY (movie_id) REFERENCES movies (movie_id),"
      "   FOREIGN KEY (genre_id) REFERENCES genres (genre_id)"
      ") ENGINE=InnoDB")


  for table_name in TABLES:
      table_description = TABLES[table_name]
      try:
          print("Creating table {}: ".format(table_name), end='')
          cursor.execute(table_description)
      except mysql.connector.Error as err:
          if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
              print("already exists.")
          else:
              print(err.msg)
      else:
          print("OK")

  cursor.close()
  cnx.close()

if __name__ == "__main__":
    main()
