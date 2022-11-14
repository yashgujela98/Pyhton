#arithematic operators
'''
+,-,/,*,%,//,**
'''
x=9
y=2
#Addition
a=x+y #9+2=11
print(a)
print("Addition is:",a)
print("Addition of",x,"and",y,"is:",a)


#Substraction
s=x-y
print("Substraction is;",s)


#Multiplication
m=x*y
print("Multi[lication is:",m)


#Division
d=x/y
print("Division is:",d)


#Modulus operator (%)
'''
This operator perform division but gives remainder of
the division operator.

mod=x%y
   =9%2                   4  Quotient
                       ---------
      Divisor--->   2|    9  dividend
                       -  8
                       -------
                          1  Remainder
'''
mod=x%y
print("Remainder is:",mod)


#True Division
'''
This operator deos diviaion but gives quotiant
'''
quo=x//y
print("Quotiant is:",quo)

#Exponent Operator(**)
'''
syntax:
         n**p where n is number and p is power
'''
exp=x**y #9**2=81
print(x,"^",y,":",exp)
