'''
WAP to find factorial of a number. take the number as input from user

5!=5*4*3*2*1

'''

n=int(input("Enter the number: "))

fact=1
i=n-1
while i>=1:

    fact=fact*i
    i-=1

print("Factorial is: ",fact)
