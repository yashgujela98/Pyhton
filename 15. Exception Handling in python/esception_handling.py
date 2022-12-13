'''
Exception
=========

Error:These are the faults or mistake in the program.
There are two types of Errors
1)Compile time error
2)Runtime Error
Compile Time Error
=================
These errors are mainly due to mistake done in writing the
syntax of the code.

Run time Error
==============
The errors which occurs during program execution are called
as Run Time Error.
mainly due to User Input or importing module which is not there
at the location.
stag1: Error checking stage.
stag2: Code execution stage.
'''
import arithematic  #Runtime error- Module not found
x=int(input("Enter numerator:"))
y=int(input("Enter denominator:")  #Compile time error or Syntax error(1st priority)

d=x/y  #9/0=> Run time error=> Exception
print("Division is:",d)
