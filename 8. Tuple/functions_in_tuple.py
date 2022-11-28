'''
Two methods or function supported in tuple.
1)count():It is  used to count occurance of the element in the
          tuple.
          
2)index():This method or function returns index of the
          elements given.

'''


t=(10,20,'Hello World',45.6,'Good morning',20,10,20)

n=t.count(20)
print(t)
print("Total number of occurence: ",n)


ipos=t.index(45.6)
print("Index position is:",ipos)

