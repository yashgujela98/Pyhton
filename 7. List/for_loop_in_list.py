#For loop over list
'''

             [10,89.7,-3,45.6,'Hello-World']
              0   1    2   3        4

'''
l=[10,89.7,-3,45.6,'Hello-World']
print("With index: ")

for i in range(0,len(l),1):    #printing using index values
    print(l[i])  


print("Without Index: ")      #printing without using index values

for i in l:  # [10,89.7,-3,45.6,'Hello-World']

    print(i)
