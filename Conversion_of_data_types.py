'''
Conversion
==========

list.,tuple and set
'''

t=(10,20,30,40)
print(t)
print(type(t))

#Convert tuple into list: 'list()' is used for thos conversion.

l=list(t)
print(l)
print(type(l))

#Change element values
l[2]=300
print(l)

#tuple(): This method is used to convert list into tuple.
tnew=tuple(l)
print(tnew)
print(type(tnew))


#Convert set into list and list to set

s={10,20,30,50}
print(s)
print(type(s))

#Convert set to list
lnew=list(s)
print(type(lnew))

#Change element values
lnew[2]=500
print(lnew)

#Change list to set
snew=set(lnew)
print(type(snew))
print(snew)

'''
To convert tuple to set we use "set_name = set(tuple_name)" and to convert set to tuple
we use "tuple_name = tuple(set_name)".
'''
