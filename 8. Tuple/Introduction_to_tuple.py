'''
Tuple
=====
1)It is collection of dissimilar datatype elements.
2)Elements in the tuple are enclosed in round brackets [parenthesis]
3)They are immutable.
'''

t=(10,20,'Hello World',45.6,'Good morning')
print(t)
print(type(t))

#len()
n=len(t)
print("Total number of elements in tuple: ",n)

#Accesing tuple elements with index
'''
''
                        t
          (10,20,'Itvedant',89.9,'Eclass')
           0  1      2       3       4
           -5-4     -3      -2      -1

     syntax:

            tuple_variable[index_pos]

            
'''



print(t[3])  #Positive indexing
print(t[-2]) #Negative indexing


#Slicing
'''
syntax:
        tuple_vairable[start:stop:step]
'''



print(t[1:4:1])
print(t[::-1])


#For loop

for i in range(0,len(t),1):

    print(t[i])


for i in t:

    print(i)
