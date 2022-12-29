'''
Destructor
=========
1.It is a special method used to delete/release memory allocated
to a object at its creation.
2.It has fixed name as __del__().
3.Destructor is called when program control reaches end.
'''


class customer:

    def __init__(self):

        print("Constructor is called")


    def __del__(self):

        print("Destructor is called")

c1=customer() #customer(c1)=> Constructor is called
c2=customer() #customer(c2)=> Construtor is called
print("Hello Wolrd")
