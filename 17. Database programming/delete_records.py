'''
Delete record from database table

query
delete from tablename where id=value;

where id=value        => search

delete from tablename => delete that record.

'''

import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="",database="company")
    cu=db.cursor()
    q="delete from employee where id=2"
    cu.execute(q)
    db.commit()
    print("Record deleted successfully")
    
except Exception as e:
    print("Error:",e)
