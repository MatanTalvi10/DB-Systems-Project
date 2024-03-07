import csv

def read_and_insert(table_name,insert_statement):
    a = 'src\\CSV files\\'
    c = '.csv'
    path = a + table_name + c
    print(path)
    with open(path, mode='r') as csv_data:
        reader = csv.reader(csv_data, delimiter=';')
        csv_data_list = list(reader)
        for row in csv_data_list:
            print(row)

add_movies = ("INSERT INTO movies(movie_id,title,release_date,runtime,adult_only) "
               "VALUES (%s, %s, %s, %s, %s)")
#read_and_insert('movies',add_movies)

with open('src\\CSV files\\movies.csv', mode='r',encoding='utf-8') as csv_data:
    reader = csv.reader(csv_data, delimiter=';')
    csv_data_list = list(reader)
    for row in csv_data_list:
        print(row)