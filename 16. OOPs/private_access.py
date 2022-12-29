'''
Private access specifier
========================
The data member and method defined as private cannot be
accessed outside class they can be accessed only inside class.

Syntax defining:

1)data member

    __variablename

2)Method

    __methodname()
'''


class student:
    def getdata(self):

        self.__name=input("Enter student name:")
        self.__rno=input("Enter roll number:")
        self.__display()

    def __display(self):
        print("Student name:",self.__name)
        print("Roll number:",self.__rno)

    
s1=student()
s1.getdata()

#print("Name:",s1.__name)   #error: cannot access private etitiy outside class
#print("Roll number:",s1.__rno)

#s1.__display()     #error: cannot access private etitiy outside class

