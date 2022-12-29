'''
Hybrid inheritance
==================
The inheritance which is the combination of Hirarchical and
multiple inheritance is called as Hybrid Inheritance.

                        A geta() => self.a
                        |
                 -----------------
                |                 |
getb()=>self.b  B                 C  self.c <= getc()
                |                 |
                 ----------------
                        |
                        D addition()

                        class A:


class B(A):


class C(A):



class D(B,C):

'''

class A:
    def geta(self):
        self.a=int(input("Enter the value of a:"))

class B(A):
    def getb(self):
        self.b=int(input("Enter value of b:"))

class C(A):
    def getc(self):
        self.c=int(input("Enter value of c:"))

class D(B,C):
    def addition(self):
        sum=self.a+self.b+self.c
        print("Addition is:",sum)


d1=D()
d1.geta()
d1.getb()
d1.getc()
d1.addition()
