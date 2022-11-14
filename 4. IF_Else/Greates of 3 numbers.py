'''
Greatest of 3 nuumbers entered by the user.
'''

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

if a>b:

    if a>c:

        print(a,"is the greatest of the 3 numbers")

    else:
        print(c,"is the greatest of the 3 numbers")

elif b>c:

    print(b,"is the greatest of the 3 numbers")

else:
    print(c,"is the greatest of the 3 numbers")
