'''

Summation of number 1 to n. take value of n from user.

step 1:
=======
n=5

sum=1+2+3+4+5=15

n=4
sum=1+2+3+4=10

      1 + 2 + 3 + 4 + 5         1 + 2 + 3 + 4
      -----                     -----
        3   + 3                   3    + 3
        -------                   --------
           6    + 4                   6    + 4
           --------                   --------
              10    + 5                   10
              ---------
                 15
step2:
       initialization=> i=1
       condition     => i<=5 (i<=n)
       incre/decre   => i+=1 or i=i+1
step 3: n=5
             s=0
          1  s=s+1
          3  s=s+2=1+2=3
          6  s=s+3=3+3=6  ====> s=s+i
         10  s=s+4=6+4=10
         15  s=s+5=10+5=15
     
        n=4
          s=0
          1  s=s+1
          3  s=s+2=1+2=3
          6  s=s+3=3+3=6  ====>s=s+i
         10  s=s+4=6+4=10

'''

n=int(input("Enter a number: "))

i=1
sum=0
while i<=n:

    sum=sum+i
    i+=1

print("Sum of first natural",n,"numbers is: ",sum)


'''
n=4
            s=0
i   i<=n    s=s+i    i=i+1
1   1<=4 T  s=0+1=1  i=1+1=2
2   2<=4 T  s=1+2=3  i=2+1=3
3   3<=4 T  s=3+3=6  i=3+1=4
4   4<=4 T  s=6+4=10 i=4+1=5
5   5<=4 F




'''
