'''
WAP to check if the number is armstrong number. get the nmber as input


n=153

sum of cube of numbers = number

1**3+5**2+3**3=1+125+27=153


'''

n=int(input("Enter a number: "))
num1=n%10
a=n//10
num2=a%10
num3=a//10

arm=(num1**3)+(num2**3)+(num3**3)

if arm==n:
    print("The number is a Armstrong Number")

else:
    print("Not a Armstrong Number")




