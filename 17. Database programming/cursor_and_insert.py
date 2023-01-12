'''
Insert record into database table
=================================
step1: connect with database.
step2: create cursor
step3: write sql query to insert rcord into database.
step4: execute that query or command or instruction.
step5: commit the changes.(save)

step2: create cursor
       cursor is a temporary space given by Database
       management system to store and execuet query.

       cu=db.cursor()
step3: write query to insert record into database table.

       insert into tablename(col1,col2,..,coln)values(val1,val2,...,valn);

       insert into employee(name,dept,sal)values('Harry','IT',70000);
step4: Execute query with cursor
       cu.execute(query)

step5: commit the changes or save it
       db.commit()
'''

import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="",database="company")
    cu=db.cursor()
    q="insert into employee(name,dept,sal)values('Rox','Support',55000)"
    cu.execute(q)
    db.commit()
    print("Record inserted successfully")
except Exception as e:
    
    print("Error:",e)
