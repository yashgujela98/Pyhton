'''
Retrieve all records from database table
=======================================
sql query to retrieve all records from database

select * from tablename;

'''

import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="",database="company")
    cu=db.cursor()
    q="select * from employee"
    cu.execute(q)
    data=cu.fetchall()
    print("Data in table:")
    print(data)
    print(type(data))
    
except Exception as e:
    print("Error:",e)


'''
                  cu.execute(q)      id  name dept  sal
     fetchall()   1                   1  Harry
data <=========   2              <=== 2  Mac
                  3                   3  Rox


'''
