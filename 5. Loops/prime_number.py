
n=int(input("Enter the number: "))

for i in range(2,n,1):

    r=n%i
    if r==0:

        print(n,"is not a prime number")
        break

else:
    print(n,"is a prime number")
        
