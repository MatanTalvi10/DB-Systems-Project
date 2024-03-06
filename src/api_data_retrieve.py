import mysql.connector
import requests
import MySQLdb as mdb
from mysql.connector import errorcode
import pandas as pd

# Loading csv content
df_department = pd.read_csv("src\CSV files\departments.csv")
df_dept_emp = pd.read_csv("src\CSV files\dept_emp.csv")
df_dept_manager = pd.read_csv("src\CSV files\dept_manager.csv")
df_employees = pd.read_csv("src\CSV files\employees.csv")
df_salaries = pd.read_csv("src\CSV files\salaries.csv")
df_titles = pd.read_csv("src\\CSV files\\titles.csv")


