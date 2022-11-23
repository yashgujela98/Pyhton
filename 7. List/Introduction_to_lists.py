'''
List
====
1)List is collection of dissimialr datatype elements.
2)Element in list are enclosed in square brackets.
3)List is mutable.(Once defined they can be changed. We can add or delete
elements from it)
'''

#Define list


print(l)
print(type(l))


#len()

n=len(l)
print("Total number of elements in the list: ",n) #===> 5

#Indexing (Positive and Negative)
'''
                       l
                       
          [10,89.7,-3,45.6,'Hello-World']
           0   1    2  3       4
           -5  -4  -3  -2      -1
           
Accessing list element
    syntax:

        list_variable[index_value]
'''

print(l[3])
print(l[-4])

#Slicing


l1=l[1:4:1]
l2=l[:4:]
l3=l[::-1]#This is reversing of the list
l4=l[:-3:-1]#reverse slicing
print(l4)
print(l2)
print(l3)
print(l1)
















