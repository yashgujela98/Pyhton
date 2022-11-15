'''
Code editor-------print()-------> console(output screen)

if there is a need to bring user input from output screen or console to the code
editor or to store in a variable, we need input() function.

syntax:
        variable=input()

step1: Give message to user         =>print()
step2: Store that input into variable => print()

'''

print("Enter first number: ")
y=input()
print("Value to y is:",y)

'''
The values entered by the user are considered as string. so 10+20 will give 1020
and not 30.
To get the correct values and perform arithmatic operations on the values entered
by the user, we need to change the datatype of the values from 'str' to 'int'
using int() function as given below
'''

x=int(input("Enter the First Value:"))
z=x+10
print("The value of z is:",z)
