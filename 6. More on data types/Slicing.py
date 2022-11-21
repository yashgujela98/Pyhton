'''
Slicing
=======
Need of slicing:
==============
If there is need to extract partial part of the string from
entire string , then use slicing.
1) to reverse string.

syntax:

string_variable[start:stop:step]

'''


x="Hello-World"

x1=x[2:8:1]
print(x)
print(x1)

#x1=x[1:8:] default step = 1 
#x1=x[:8:] default start = 0
#x1=x[::] default stop = string end



'''
Slicing with negative index/step
================================

                    H   E   L   L   O   -   W   O   R   L   D
                    0   1   2   3   4   5   6   7   8   9   10
                  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0

Step => Negative
if step is negative then rightmost index is considered as start.

If step is positive, start is leftmost index
'''

x1=x[10:8:-1] #14,13,12,11,10,9
x1=x[:8:-1]  #start: 10 because negative step
x1=x[::-1]  #start=10(rightmost index), end=0(leftmost index), because step=-1
print(x1)
