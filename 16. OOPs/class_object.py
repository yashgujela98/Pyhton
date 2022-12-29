#Data members and methods


class student:
    def getdata(self):

        self.name=input("Enter student name:")
        self.rno=input("Enter roll number:")

    def display(self):

        print("Student name:",self.name)
        print("Student roll number:",self.rno)


s1=student() #object created
s1.getdata() #getdata(s1)
s1.display()

s2=student()
s2.getdata()
s2.display()
