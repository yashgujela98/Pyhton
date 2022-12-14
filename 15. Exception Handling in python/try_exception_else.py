'''
try...exception and else
========================
else block is executed only when there is no exception.
'''


try:
    x=int(input("Enter numerator:"))    #two => Exception
    y=int(input("Enter denominator:"))  #0 and two => Exception
    d=x/y
    

except Exception as x:

    #print("Something went wrong !!!")
    print("Error: ",x)

else:

    print("In else block")
    print("Division is:",d)


'''
else block is used to offload try block.
try block should always contain only those lines of code
in which there is chance of getting error.
code lines in which there is no chance of getting run time
error or exception must be in else block.
'''
