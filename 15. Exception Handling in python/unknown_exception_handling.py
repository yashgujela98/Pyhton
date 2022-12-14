'''
Handling exception when the error is unknown.

finally block is executed in both situation
1)If there is exception.
2)If there is no exception.
'''

try:
    x=int(input("Enter numerator:"))    #two => Exception
    y=int(input("Enter denominator:"))  #0 and two => Exception
    d=x/y
    print("Division is:",d)

except Exception as x:

    #print("Something went wrong !!!")
    print("Error: ",x)

finally:

    print("Inside Finally Block")

'''
Whenever a transation of inserting record, retrieve records
update record and delete record with the database is
completed, it is a good practice to close connection of
your code with database, so that data is secured.

      python ---Connection----> Database [to perform operations]

And even if exception arises, then connection to the database
must be closed.

'''
