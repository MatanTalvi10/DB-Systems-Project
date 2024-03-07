import mysql.connector
import requests
import MySQLdb as mdb
from mysql.connector import errorcode
import pandas as pd

# Loading csv content
df_department = pd.read_csv("src\CSV files\departments.csv")
df_emp_dept = pd.read_csv("src\CSV files\emp_dept.csv")
df_managers_dept = pd.read_csv("src\CSV files\managers_dept.csv")
df_employees = pd.read_csv("src\CSV files\employees.csv")
df_wages = pd.read_csv("src\CSV files\wages.csv")
df_positions = pd.read_csv("src\\CSV files\\positions.csv")

def insert_department(csv_file)


