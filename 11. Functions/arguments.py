'''
Arguments:
==========
Values or variables that are passed by the function call to the function defination
or body is called as arguments.

    Number of arguments or        Number of varaible used to
    values passed            =     recieve.
    
'''
#addition of 2 integers.
def add(a,b):

    add=a+b

    print("Addition=",add)

add(5,20)       #function call. a=5 and b=20


#sum of 1 to n integers.
def sum(s,n):

    for i in range(1,n):

        s+=i

    print("Sum=",s)

sum(0,10)      #function call. s=0 and n=10




