'''
syntax:

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

a=lambda x,y:x+y

res=a(20,30)  #lambda call

print("Addition is:",res)
