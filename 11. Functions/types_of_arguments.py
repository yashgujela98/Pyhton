'''
Default arguments
=================
                 Number of arguments or        Number of varaible used to
                 values passed           =     recieve.
'''
def add(a,b):

    s=a+b
    print("Addition=",s)

#add(10) error as 'y' value is not passed.


def addition(a,b=20):       #b=20 is default argument.

    s=a+b
    print("Addition=",s)

addition(10)#no error because it considers default b value

addition(10,10) #here it considers the the values passed. if no value is passed 
                #then default value is considered.



'''
Key value argument
==================
 key=value


   area of rectangle=length x breadth

           3
    ---------------
   |               |
   |               | 2    area=3x2=6
   |               |
    ---------------
'''

def area(l,b):

    print("Length: ",l)
    print("Breadth: ",b)

    area=l*b

    print("Area: ",area)

area(10,20)     #Required parameter
area(20,10)     #required paramter

#although the area is same but the length and breadth is different.
area(l=10,b=20)  #Key value argument
area(5,b=20)     #here l=5,b=20. area(10,l=20) will be an error.

'''
Variable length argument
========================
Variable: changing

Length: number of arguments

'''

def addition(*x):   #*x means it can have multiple values.
    sum=0
    for i in x:

        sum+=i

    print("Sum is: ",sum)

addition(20,30,40)
addition(10,20)

'''
Variable length argument ==> Key value pair
'''

def ad(**y):   #*=>key and *=>value

    print(y)
    print(type(y))
    s=0
    for i in y:

        s+=y[i]

    print("Summation is: ",s)


ad(a=10,b=20)
ad(a=10,b=20,c=30)
ad(a=10,b=20,c=30,d=40)
    



























