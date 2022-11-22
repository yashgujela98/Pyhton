'''
WAP to find factorial of a number. take the number as input from user
5!=5*4*3*2*1
'''

n=int(input("Enter the number: "))

fact=1

for i in range(1,n+1):

    fact=fact*i
    
print("Factorial of",n,"is:",fact)
