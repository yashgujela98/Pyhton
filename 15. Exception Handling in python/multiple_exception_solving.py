'''
Handling Multiple Exception
===========================

try:

    code to be insepected for Exception
    or
    code in which there is chance of
    getting execption.

except ExceptionName1:

   except block to given msg.

except ExceptionName2:

   except block to given msg.

.
.
.
except ExceptionNameN:

   except block to given msg.

'''


try:
    x=float(input("Enter numerator:"))    #two => Exception
    y=float(input("Enter denominator:"))  #0 and two => Exception
    d=x/y
    print("Division is:",d)

except ZeroDivisionError:

    print("Denominator cannot be zero")

except ValueError:

    print("Enter an integer or decimal number")
