'''
Custom Exception
===============
Creating or definig your own exception other that built in
exception.
If you want your error name to be recognised as python exception
it must be derived from the base class Exception
'''
class ErrorError(Exception):
    pass

x=float(input("Enter numerator:"))
y=float(input("Enter denominator:"))

if y==0:
    raise ErrorError("Denominator cannot be zero!!")

else:
    d=x/y
    print("Division is:",d)



    
