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
def create_tables():
    DB_Name = "employees"
    TABLES = {}

    # Creating departments table
    TABLES['departments'] = (
        "CREATE TABLE 'departments' ("
        "   'dept_id' VARCHAR(50) NOT NULL,"
        "   'dept_title' varchar(50) NOT NULL,"
        "   PRIMARY KEY ('dept_id')"
        ") ENGINE=InnoDB")

    # Creating positions table
    TABLES['positions'] = (
        "CREATE TABLE 'positions' ("
        "   'position_id' VARCHAR(50) NOT NULL,"
        "   'position' varchar(50) NOT NULL,"
        "   PRIMARY KEY ('position_id')"
        ") ENGINE=InnoDB")

    # Creating employees table
    TABLES['employees'] = (
        "CREATE TABLE 'employees' ("
        "   'employee_id' INT NOT NULL,"
        "   'emp_title_id' VARCHAR(50) NOT NULL,"
        "   'birth_date' VARCHAR(50) NOT NULL,"
        "   'first_name' VARCHAR(50) NOT NULL,"
        "   'last_name' VARCHAR(50) NOT NULL,"
        "   'gender' VARCHAR(10) NOT NULL,"
        "   'start_date' VARCHAR(50) NOT NULL,"
        "   PRIMARY KEY ('employee_id'),"
        "   FOREIGN KEY ('emp_title_id') REFERENCES 'positions' ('position_id')"
        ") ENGINE=InnoDB")

    # Creating emp_dept table
    TABLES['emp_dept'] = (
        "CREATE TABLE 'emp_dept' ("
        "   'employee_id' INT NOT NULL,"
        "   'dept_id' VARCHAR(50) NOT NULL,"
        "   PRIMARY KEY ('employee_id','dept_id),"
        "   FOREIGN KEY ('employee_id') REFERENCES 'employees' ('employee_id'),"
        "   FOREIGN KEY ('dept_id') REFERENCES 'departments' ('dept_id')"
        ") ENGINE=InnoDB")

    # Creating managers_dept table
    TABLES['managers_dept'] = (
        "CREATE TABLE 'managers_dept' ("
        "   'dept_id' VARCHAR(50) NOT NULL,"
        "   'employee_id' INT,"
        "   PRIMARY KEY ('dept_id','employee_id),"
        "   FOREIGN KEY ('employee_id') REFERENCES 'employees' ('employee_id')"
        ") ENGINE=InnoDB")

    # Creating wages table
    TABLES['wages'] = (
        "CREATE TABLE 'wages' ("
        "   'employee_id' INT,"
        "   'wage' INT,"
        "   PRIMARY KEY ('employee_id'),"
        "   FOREIGN KEY ('employee_id') REFERENCES 'employees' ('employee_id')"
        ") ENGINE=InnoDB")

