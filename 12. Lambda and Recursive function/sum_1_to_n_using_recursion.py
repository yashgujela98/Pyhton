'''
Summation of 1 to n using Recursion.
n=5
1+2+3+4+5=15
'''
num=int(input("Enter last term in the series:"))
def add(n):

    if n==1:

        return 1

    r=n+add(n-1)

    return r

res=add(num)
print("Sum is:",res)

'''
res=summtion(4)=>10
   |
   |
def summation(4):  ----def summation(3): --def summation(2): ---def summation(1):
                  |                     |                   |
    if 4==1: F    |      if 3==1: F     |    if 2==1: F     |     if 1==1: T
                  |                     |                   |        return 1
  10r=4+summation(3)    6r=3+summation(2)    3r=2+summation(1)              |
      |        |           |        |           |           |               |
    return(10)

'''
