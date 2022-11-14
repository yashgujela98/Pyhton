'''
Greatest of 3 numbers using logical operators.
'''
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

if a>b and a>c:
    print(a,"is the greates of the 3 numbers")

if b>a and b>c:

    print(b,"is the greates of the 3 numbers")

if c>a and c>b:

    print(c,"is the greatest of the 3 numbers")


'''
In user input of a=70,b=50,c=20
First if condition is evaluated to be True and we
got the result of greatest of three numbers.

If we got the result in first if condition, then
ideally there is no need to check further if conditions.
Since in above program its checking other two condition,
there is waster of interpreter time in code execution
which is not  going to give us output.



'''
