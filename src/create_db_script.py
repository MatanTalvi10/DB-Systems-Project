import mysql.connector
import requests
import MySQLdb as mdb
import json
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='matantalvi', password='mata10092',
                              host='localhost',
                              database='matantalvi',port= 3305)
cnx.close()
