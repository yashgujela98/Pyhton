
#Add element in the list
'''
There are two methods or function to add
element in the list.
1)append():
   This function or method is used to add element at the
   end of the list.
   syntax:
          list_variable.append(element)
2)insert():
  This function or method is used to add element at
  specific index position

  list_variable.insert(index_pos,value)


                            l
                            
            [ 10,89.7,-3,45.6,'Hello World']
              0   1    2   3       4          

'''
l=[10,89.7,-3,-45.6,'Hello World','Good morning']

l.append(24.5)
print(l)

l.insert(3,50)
print(l)


#update list element
'''
syntax:

     list_variable[index_pos]=value

'''

l[4]="Hello-World"
print(l)


#delete or remove list elements.
'''
pop(): This is used to delete last elements.

pop(index):This remove specific element whose index is
mentioned in the pop() method.


                            l
                            
            [ 10,89.7,-3,45.6,'Hello-World',24.5,'Good morning']
              0   1    2   3       4          5        6
'''


l.pop()
print(l)
'''
                                l
                            
            [ 10,89.7,-3,45.6,'Hello-World',24.5]
              0   1    2   3       4          5        
'''

l.pop(2)
print(l)
'''
                    [ 10,89.7,45.6,'Hello-World',24.5]
                      0   1    2          3       4            
'''


#del: keyword used to delete entire list at once

del l

print(l)






