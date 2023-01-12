'''
Connecting python with Mysql Database Management System.
=======================================================


Python and mysql are different platform. In order to
establish connection between python and mysql, there is need
of connector.
That connector is called as pymysql module.
python                         mysql
                             pymysql
              .py file ------------------->  database

To install any external module use following command on
cmd prompt.
syntax:

pip install modulename

e.g install pymysql
pip install pymysql
pip is a package installation manager, whose duty is to
download and install all readymade packages in python.

connect():This function connect python with mysql database

syntax:

pymysql.connect(host="localhost",user="root",password="",
                database="databasename")

pymysql.connect(host="localhost",user="root",password="",
                database="company")
fp=open("data.txt",'r')
fp was a reference object of data.txt file in python.


db=pymysql.connect(host="localhost",user="root",password="",
                database="company")

db is a reference object of that database in python file
'''

import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="",database="company")
    print("Connected Succesfully")
    
except Exception as e:
    
    print("Error:",e)
