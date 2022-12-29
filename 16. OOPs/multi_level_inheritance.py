'''
Multilevel inheritance
=====================
                          A Base class
                          |
                          |
                          B Intermediate base class
                          |
                          |
                          C Intermediate base class
                          |
                          |
                          |
                          D derived class
                          

'''

class A:

    def geta(self):
        self.a=int(input("Enter value of a:"))

class B(A):

    def getb(self):
        self.b=int(input("Enter value of b:"))

class C(B):

    def getc(self):
        self.c=int(input("Enter value of c:"))

class D(C):

    def addition(self):
        res=self.a+self.b+self.c
        print("Addition is:",res)

d1=D() #derived class object is created
d1.geta() #geta(d1)
d1.getb() #getb(d1)
d1.getc() #getc(d1)
d1.addition() #addition(d1)





