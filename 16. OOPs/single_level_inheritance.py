'''
Single Inheritance:
==================
The inheritance in which there is only one base class and
one derived class is called as Single inheritance.

                         A base class
                         |
                         |
                         |
                         B Derived class
                         
In class A

method     =>geta()
data member=>a

class B
method      => getb()
data member => b
'''

class A:

    def geta(self):

        self.a=int(input("Enter value of a:"))

class B(A):

    def getb(self):
        self.b=int(input("Enter value of b:"))


    def addition(self):

        res=self.a+self.b
        print("Addition is:",res)


b1=B() #derived class object
b1.geta() #geta(b)
b1.getb() #getb(b)
b1.addition() #addition(b1)
