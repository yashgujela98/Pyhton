'''
Raising an exception
====================
                                                                ------ Python
When ther is fault in runtime--Exception is raised--handled by-|
                                    by system                   ------ try..except

Till now exception is raised internally by system,
if there is need to raise an exception , then
use raise keyword to raise an exception.

exeception is raised with respect to certain condition.
syntax to raise exception

'''

x=int(input("Enter numerator:"))    #two => Exception
y=int(input("Enter denominator:"))  #0 and two => Exception

if y==0:

    raise ZeroDivisionError("Denominator cannot be zero!!!")

else:
    d=x/y
    print("Division is:",d)
