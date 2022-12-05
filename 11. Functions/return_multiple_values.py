'''
WAP to show the concept of multple values returns and store them when called.

When we return 2 values, we have to take 2 variables in the call and store those
returned values int them.

eg:

        return add,sub

    a,b=def_functionname()

Here 'a' will store the value of 'add' and 'b' of 'sub'.
Now they can we used later on in the program.
'''

n1=int(input("Enter firdt value:"))
n2=int(input("Enter second value"))


def arithmetic(x,y):

    add=x+y
    sub=x-y
    mul=x*y
    div=x/y


    return add,sub,mul,div  #Multiple retun value

a,b,c,d=arithmetic(n1,n2)   #no of variable to store=no of returned values in the same order as returned.

print("Addition:",a)
print("Substraction:",b)
print("Multiplication:",c)
print("Division:",d)
