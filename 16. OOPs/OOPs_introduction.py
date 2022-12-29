'''
Types of Programming
====================
1)Procedural oriented programming
2)Object Oriented programming

Need of OOPS
============

Procedural oriented programming system
====================================== 
The programming system in which contains inbuilt
functions or user defined functions to executed
a task or logic is called  as Procedural programming system.
1.Security
========
In procedural oriented programming system, a global variable
value can be accessed in all functions, this may create an
issue of security for a global variable storing sensitive
information like username and password.


2.user defined Datatype
=======================
int,float and string these are built in datatypes.If there is
need to create user defined datatype, then it can be achived
with the help of OOPS.
In order to remove disadvantage of Security in procedural
programming system and to create user defined datatype ,mapping
real world entity digitially,there is need of OOPS.

Object Oriented Programming system consist of:
1)classes
2)objects
class
=====
class is a template or blueprint.

Object
======
Object is manufactured from class blueprint.


                       student name:______________
                       Roll number :______________  ===> Blueprint
                       per         :______________  

                       Submit
shirish patil19:23
|
            ------------------------------------
          |                                     |

student name:Itvedant               Student name: Eclas   
Roll number :45                     Roll Number : 35
per         :98                     per         : 87.9

       object 1                          object 2

'''

uname=input("Enter user name:")
upass=input("Enter password:")

def greet():
    print("Good Evening")
    print("Value of uname is:",uname)

def helloworld():

    print("Hello world")
    print("Value of upass is:",upass)

greet()
helloworld()
