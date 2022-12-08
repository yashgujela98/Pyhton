#String Constants

import string as s

print(s.ascii_lowercase)
print(s.ascii_uppercase)
print(s.ascii_letters)


s="Hello World"

sup=s.upper()
print(sup)  #Uppercase

slow=s.lower()
print(slow) #Lowercase

#isalpha()
'''
This method check whether entire string contains alphabets.
If all string elements are alphabets then it return True
or it returns False.
'''

a="Hello-World"  #False because of '-'
b="Hello World"  #False because Space ' '
c="HelloWorld"   #True because all alphabets

q=c.isalpha()
print(q)
p=b.isalpha()
print(p)
r=a.isalpha()
print(r)


#isdigit()
'''
This method is used to check whether string elements are
digits i.e 0,1,2,3,...9
It returns True if string contains all digits.
It returns False if string contains other than digit.
'''

d="12345a"
f=d.isdigit()
print(f)

#split()
'''
When there is a need to convert string into a list, split() method is used

syntax:
        str_variable.split('seperator')
'''

str="We are learning-String methods-in today's-session"
str2="We are learning,String methods,in today's,session"

l1=str.split('-')
l2=str2.split(',')
print(l1)
print(l2)
print(type(l1))
print(type(l2))
#If we dont give a seperator, by default it will consider space(' ') as a seperator.


















