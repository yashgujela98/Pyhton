'''
built in modules
================

                         modules
                            |
                --------------------------
               |            |             |
             Functions    Constants    Classes

In order to use math module in the python file. Then
there is s need to import that module

step1: import module
step2: use that module
'''

import math
n=int(input("Enter a number:"))
#factorial

r=math.factorial(n)
print("Factorial of number is:",r)


#Alisaing module

import math as m

#ciel() and floor()

'''
ceil()
15.7 => 15 to 16 => 16
15.5 => 15 to 16 => 16
15.2 => 15 to 16 => 16
'''

print(m.ceil(15.8))
print(m.ceil(15.5))
print(m.ceil(15.2))

'''
floor()
15.8 => 15 to 16 => 15
15.5 => 15 to 16 => 15
15.2 => 15 to 16 => 15
'''

print(m.floor(15.8))
print(m.floor(15.5))
print(m.floor(15.2))


#Import specific functionality

from math import factorial,sqrt

r=factorial(6)
print("Factorial is:",r)

sroot=sqrt(25)
print("Square root is:",sroot)

#Import everything from module

from math import *

print(ceil(15.2))
print(floor(15.8))
print(factorial(4))
print(sqrt(4))

#Similarly we can use various functions of different modules.















