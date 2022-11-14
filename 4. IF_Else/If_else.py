'''
A number is entered by User. Write a program to check whether
number is even or odd number.

even: The number which is completely divisible by 2.
      Since it is completely division its remainder of
      the division is Zero.
      opertor:%
step1:start
step2:message to user.=> print()
step3:store that input in variable.=>input()
step4:calculate remainder
step5:if remainder is equal to 0 then it is even
step6:if remainder is not equal to 0 then it is odd..
step7:stop
'''
'''
print("Enter number: ") #16,25
n=int(input()) #n=16,25
r=n%2 #r=16%2=1

if r==0: #0==0 T, 1==0 F
    print("Even Number")

else:
    print("Odd Number")
'''

x=int(input("Enter the number: "))

if x>0:
    print("Positve Number")

else:
    print(" Negative")
