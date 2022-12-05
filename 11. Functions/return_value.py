'''
Syntax:

def function_name(arguments):

    function body

    return value

Need: If there is need for a function to return a value or
      result there use return statement.
Problem:
=======
values given to function=>marks of 3 subjects
definition of function  =>Calculate total

%  = marks obtained           marks obtained
     -------------- x 100  => ---------------  
        300                          3

returned value is returned at the place of the function call.
Thus we require a variable to which function call is assigned
so that returned value is stored in that variable.
'''

sub1=int(input("Enter the marks for subject 1:"))
sub2=int(input("Enter the marks for subject 2:"))
sub3=int(input("Enter the marks for subject 3:"))


def marksadd(a,b,c):

    t=a+b+c
    
    return t

tot=marksadd(sub1,sub2,sub3)  #returned value 't' is stored in 'tot'

print("Total marks:",tot)     #here 'tot' will return the value of 't' outside its function
per=(tot/300)*100             #after storing retuned value we can use it elsewhere in the program.
print("Percentage:",per)
