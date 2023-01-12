'''
updating a specific record
==========================
Harry=>Hari  IT=>CS  70000=>90000

sql query to update a record
----------------------------
update tablename set colname1=newval1,colname2=newval2,...
                     colnamen=newvaln where id=value

In update is done in two steps
1) serach a record => where id=value
2) update record   => set colname1=newval1,colname2=newval2,...
                     colnamen=newvaln
'''

import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="",database="company")
    cu=db.cursor()
    q="update employee set name='Hari',dept='CS',sal=90000 where id=1"
    cu.execute(q)
    db.commit()
    print("Record updated successfully")
    
    
except Exception as e:
    print("Error:",e)
