'''
Summation of 1 to n using for
'''

n=int(input("enter the last number: "))
s=0
for i in range(1,n+1,1):

    s=s+i

print("Sum is: ",s)


'''
i   i in []   s=s+i    i step 1
1   1 in[]T   s=0+1=1  2
2   2 in[]T   s=1+2=3  3
3   3 in[]T   s=3+3=6  4
4   4 in[]T   s=6+4=10 5
5   5 in[]F
'''
