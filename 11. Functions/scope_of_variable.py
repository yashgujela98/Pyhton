'''
Scope of Variable
=================

The region in the program where value of the variable can be accessed is called
as scope of varaible.

There are 2 types of scopes:

1)Local variable scope
2)Global varaible scope

Global variable scope
=====================

The variable that is defined outside the function and whose value can be
accessed inside the function is called global variable.
'''

x=10
print("Value of variable is: ",x)

def scope_variable():

    print("Value of variable inside function: ",x)


scope_variable()

'''
Local variable scope
====================
Variable defined in the function or in a scope has life or accessibilty to its
value within that scope only, it cannot be accessed outside that scope.
This type of variable is called as local variable.

'''

def local_scope_variable():
    y=50    #local variable. defined in function and accessed in it only.
    print("Value of variable inside function: ",y)


local_scope_variable()

#print("value of variable outside function: ",y) ERROR variable accessed outside function
