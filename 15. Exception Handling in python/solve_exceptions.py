'''
Handling exception can be done using following instruction.

try:

    code to be insepected for Exception
    or
    code in which there is chance of
    getting execption.

except ExceptionName:

   except block to given msg.
'''

x=float(input("Enter numerator:"))
y=float(input("Enter denominator:"))

try:
    d=x/y
    print("Division is:",d)

except ZeroDivisionError:

    print("Denominator cannot be zero")
