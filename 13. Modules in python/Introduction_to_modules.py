'''
Need of Module
==============

Reusing functionality across various python files.

    one.py                two.py                third.py
-----------------      ----------------      ----------------

def addition(x,y):     def addition(x,y):  def addition(x,y):

  z=x+y                 z=x+y               z=x+y
  print(z)              print(z)            print(z)
In above example function addition is defined in all the files
which led to repeatition of code.

In order to avoide this repeatition of code,create a python
file and define addition function in the python file and import
that python file in another python files such as one.py,two.py
, three.py.
The python file that is imported in another python file is called
as Module in python.
arithmetic.py => module
                             -------------
                             def addition(x,y):
                               z=x+y
                               print(z)
                                 |
            --------------------------------------------
           |                     |                      |
        one.py                two.py                 three.py
what  is module?
================
Module is a python files which is collection of functions,
constants and classes.

Types of modules
================
1)built in modules
2)user defined Modules
3)packages
'''
