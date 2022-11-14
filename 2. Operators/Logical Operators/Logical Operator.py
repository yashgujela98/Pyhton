#Logical Operators
'''
Need of Logical Operators
=========================
1) To check more than one condition in conditional statement or instruction.
'''

x=10
y=20
z=40

r= x>y and x>z #10>20 and 10>40 => False and False => False
               #100>20 and 100>40 => True and True => True
print(r)

#OR Operator

a=10
b=25
c=9

re=a>b or a>c #10>25 or 10>9 => False or True => True
print(re)

#Unary Operator NOT(!)

renot=not(a>b) #!(10>25) => !(False) => True
print(renot)
