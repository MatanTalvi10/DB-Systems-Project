import pandas as pd
import csv
import numpy as np

#df_rating = pd.read_csv("src\\CSV files\\ratings.csv")

df_movies = pd.read_csv("src\\  CSV files\\movies.csv")


print(df_movies.head())
#print(df_rating.head())

'''
# Filter rows in df_rating where movie_id does not exist in df_movies
df_rating = df_rating[~df_rating['movie_id'].isin(df_movies['movie_id'])]

# Reset index after filtering
df_rating.reset_index(drop=True,inplace=True)


print(df_rating.head())

print(df_rating.tail())

df_rating.to_csv('pd_rating1.csv',index=False) 
'''