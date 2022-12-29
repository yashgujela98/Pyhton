'''
Inheritance
===========

Need
-----
e.g:

class A:

   def getdata(self):

      .......
      .......

   def displayA(self):

      ........
      ........
class B:

   def getdata(self):
      .......
      .......

   def displayB(self):
      ........
      ........
Method getdata() defined in class A, same method is required
in class B, as a result we need to rewrite that method again
in the class B which give rise to code repeatition.

In order to reuse the property of one class into another class
there is need of inheritance.
what is inheritance?
===================
The mechanism or process of deriving one class from another class
to achieve reusability of code is called as Inheritance.

The class from which another class is derived is called as
Base class or parent class.

The class which is derived from another class is called as
derived class or child class.
A  parent or base class
                            |
                            |
                            |
                            B child or derived class

Properties of class A or base class [data member and methods]
are now available to derived class or child class.


Syntax for derived class
=======================

class Derivedclassname(baseclassname):

      derived class Body

e.g:

class A:

    body of class A


class B(A):

   body of class B


Type of Inheritance:
===================
1)Single inheritance
2)Multilevel inheritance
3)Multiple inheritance
4)Hierarchical Inheritance
5)Hybrid Inheritance
