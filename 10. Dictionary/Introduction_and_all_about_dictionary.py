'''
1)Dictionary is also a collection of dissimilar elements.
2)Elements in dictionary are arranged in key:value format.
3)They are mutable.
4)keys are unique and values can be duplicated.
5)Elements are enclosed in curly braces.

'''

d={'a':'apple','b':'ball',2:'two',10:100}
print(d)
print(type(d))

#len()
n=len(d)
print("Total number of elements in dictionary: ",n)

#Indexing or accessing with index is not possible

#We can acccess values using key
'''
        dictionary_variable[keyname]
'''
print(d['b']) #'b' is a key and value is 'ball'
print(d[10])

#Slicing is also not possible because of no index

#For loop with index is not possible
#For loop without index

for x in d:#{'a':'apple','b':'ball',2:'two',10:100}
    print(x)     #'a','b',2,10
    print(d[x])  #d['a']='apple',d['b']='ball',d[2]='two',d[10]=100
    print(x,":",d[x])


#Add element: Adds element to the last of the dictionary

d['c']='cat'
print(d)

#Update Element: Updates the value of the key.

d['a']='Air'
print(d)

#Remove elements
'''
pop()
syntax:
        d.pop(keyname)
'''

d.pop(2)
print(d)

#Deletes entire dictioanary. syntax: del dictionary_variable

del d
print(d) #Gives error
