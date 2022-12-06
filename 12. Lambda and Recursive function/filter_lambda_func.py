'''
Application
===========
If there is need to pass a function as an argument to
another function, we use lambda function to pass as
argument to another function.

filter()

syntax:
filter(function,iterables)
iterables can be list, tuple or set.

function argument in filter() is a lambda function which
contains condition which must be satisfied by the element in
the iterable to get filtered.

'''

l=[1,-9,-8,56,47,-2,45,78,-6]

lpos=list(filter(lambda x:x>0,l))
print(lpos)


'''
Note: filter() function returns filter object which contains
result. Thus to see result there is need to convert that
filter object into respective data type i.e in list,tuple
and in set.
1st call    lambda 1:1>0  T  1 is stored in result list
2nd call    lambda-9:-9>0 F  -------
3rd call    lambda-8:-8>0 F  -------
4th call    lambda56:56>0 T  1,56 is stored

'''
