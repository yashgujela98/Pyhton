'''
print table of any number entered by user.
step1: Example
      2=2*1    3=3*1
      4=2*2    6=3*2
      6=2*3    9=3*3
      8=2*4    .
     10=2*5    .     ====> r=2*i where i takes value from 1 to 10
     12=2*6    .
     14=2*7    .
     16=2*8    .
     18=2*9    .
     20=2*10  30=3*10
step2:     repeatition=>loop
     loop
     1)initialization  i=1
     2)condition       i<=10
     3)incre/decre     i+=1 or i=i+1
step3:
     body=> code to be repeated
     r=2*i
'''
n=int(input("Enter a number: "))


i=1

while i<=10:

    r=n*i
    print(r)

    i+=1
    
'''
i   i<=10   r=2*i     print(r)     i+=1 or i=i+1
1   1<=10   r=2*1=2   2            i=1+1=2
2   2<=10T  r=2*2=4   4            i=2+1=3
3   3<=10T  r=2*3=6   6            i=3+1=4
4
5
6
7
8
9
10  10<=10T r=2*10=20 20           i=10+1=11
11  11<=10F
'''
