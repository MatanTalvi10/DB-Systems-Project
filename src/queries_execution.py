import queries_db_script as qdb


# 1   
qdb.query_1('Love')
'''
This query returns all the columns of the movies table but only 
for movies with the word 'Love' in their title
'''

# 2   
qdb.query_1('King')
'''
This query returns all the columns of the movies table but only 
for movies with the word 'king' in their title
'''

# 3   
qdb.query_2()
'''
Counts the number of movies in each genre according to predetermined buckets of budget.
'''

# 4   
qdb.query_3()
'''
Lists the movies and their genre with their average rating by all users.
'''

# 5   
qdb.query_4(1)
'''
return the names of the movies user_id = 1 rated and the ratings for each movie.
'''

# 5   
qdb.query_4(2)
'''
return the names of the movies user_id = 1 rated and the ratings for each movie.
'''

# 5   
qdb.query_5(2)
'''
return the names of the movies user_id = 1 rated and the ratings for each movie.
'''