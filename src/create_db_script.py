import mysql.connector
from mysql.connector import errorcode

'''
cnx = mysql.connector.connect(user='matantalvi', password='mata10092',
                              host='localhost',
                              database='matantalvi',port= 3305)
cnx.close()
'''
DB_Name = "employees"
TABLES = {}

# Creating departments table
TABLES['departments'] = (
    "CREATE TABLE 'departments' ("
    "   'dept_no' VARCHAR(50) NOT NULL,"
    "   'dept_name' varchar(50) NOT NULL,"
	"   PRIMARY KEY ('dept_no')"
    ") ENGINE=InnoDB")

# Creating titles table
TABLES['titles'] = (
    "CREATE TABLE 'titles' ("
    "   'title_id' VARCHAR(50) NOT NULL,"
    "   'title' varchar(50) NOT NULL,"
	"   PRIMARY KEY ('title_id')"
    ") ENGINE=InnoDB")

# Creating employees table
TABLES['employees'] = (
    "CREATE TABLE 'employees' ("
    "   'emp_no' INT,"
    "   'emp_title_id' VARCHAR(50) NOT NULL,"
    "   'birth_date' VARCHAR(50) NOT NULL,"
    "   'first_name' VARCHAR(50) NOT NULL,"
    "   'last_name' VARCHAR(50) NOT NULL,"
    "   'sex' VARCHAR(10) NOT NULL,"
    "   'hire_date' VARCHAR(50) NOT NULL,"
    "   PRIMARY KEY ('emp_no'),"
    "   FOREIGN KEY ('emp_title_id') REFERENCES 'titles' ('title_id')"
    ") ENGINE=InnoDB")

# Creating dept_emp table
TABLES['dept_emp'] = (
    "CREATE TABLE 'dept_emp' ("
    "   'emp_no' INT,"
    "   'dept_no' VARCHAR(50) NOT NULL,"
    "   PRIMARY KEY ('emp_no','dept_no),"
    "   FOREIGN KEY ('emp_no') REFERENCES 'employees' ('emp_no'),"
    "   FOREIGN KEY ('dept_no') REFERENCES 'departments' ('dept_no')"
    ") ENGINE=InnoDB")

# Creating dept_manager table
TABLES['dept_manager'] = (
    "CREATE TABLE 'dept_manager' ("
    "   'dept_no' VARCHAR(50) NOT NULL,"
    "   'emp_no' INT,"
    "   PRIMARY KEY ('dept_no','emp_no),"
    "   FOREIGN KEY ('emp_no') REFERENCES 'employees' ('emp_no')"
    ") ENGINE=InnoDB")

# Creating salaries table
TABLES['salaries'] = (
    "CREATE TABLE 'salaries' ("
    "   'emp_no' INT,"
    "   'salary' INT,"
    "   PRIMARY KEY ('emp_no'),"
    "   FOREIGN KEY ('emp_no') REFERENCES 'employees' ('emp_no')"
    ") ENGINE=InnoDB")

