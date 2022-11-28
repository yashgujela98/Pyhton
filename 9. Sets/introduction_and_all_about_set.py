'''
Set
===

1)Set is collections of dissimilar datatype elements.
2)sets are enclosed within curly braces {}
3)sets are mutable.
4)sets are unordered.
   In other data types index position of the element is fixed.
   but in set position of the element changes.
5)sets allows only unique values[no duplication].
'''


s={10,20,'Hello World',45.6,'Good morning'}

print(s)
print(type(s))

#len()
n=len(s)
print("Total number of elements in set are: ",n)

#print(s[1]) Sets dont have any index value. They are unordered

#Indexing or accessing elements is not possible in sets.

#Slicing which requires index is not possibe in set.

#For loop with index- not possible
#For loop without index

for x in s: #10,20,'Hello-World',45.6,'Good Morning'

    print(x)


#Add element in the set
'''
add(): This function is used to add element in the set.

  set_varianle.add(value)
'''

s={10,20,'Hello World',45.6,'Good morning'}
s.add(58)
print(s)

#Updating an existing value is not possible in set because of no index

#Delete or remove element from set
'''
set_variable.remove(value)
'''

s.remove(58)
print(s)

del s #deletes the entire set























    
