'''
Find summation of the integer elements in the list.

                l
        [10,20,35,1,2,-3]
         0  1  2  3 4  5

         sum=0
sum=sum+10=0+10=10
         sum=sum+20=10+20=30
         sum=sum+35=30+35=65  ===> sum=sum+i
         sum=sum+1=65+1=66
         sum=sum+2=66+2=68
         sum=sum+(-3)=sum-3=68-3=65

         sum=sum+l[0]
         sum=sum+l[1]
         sum=sum+l[2]===> sum=sum+l[i]
         sum=sum+l[3]
         sum=sum+l[4]
         sum=sum+l[5]
'''


l=[10,20,35,1,2,-3]

print(l)
sum=0

for i in l:

    sum+=i

print("Summation of the list elements is: ",sum)
