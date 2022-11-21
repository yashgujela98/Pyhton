'''
String:
'''


#len(): This is used to calculate number of characters in the string.

x="Itvedant-eclass"

n=len(x)
print("Total number of character: ",n)


'''
Need: To process string characte by charatcer, there is need to access character
in the string. Indexing helps you to access charater in string.

There are 2  types of indexing:
1) Positive indexing
2) Negative indexing

Positive Indexing
=================
                                     x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Negative Indexing
=================

          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

Syntax for accessing:
====================
 string_variable[index_number]

'''

print(x[7])
print(x[12])
#print(x[16])=> #error-> index out of range
print(x[-11])
print(x[-14])
