'''
Find number of vowels and consonants in the string entered by the user.
'''

str=input("Enter a string: ")
count=0
c=0
for i in str:
    

    if i in('a','e','i','o','u','A','E','I','O','U'):
        count+=1
    else:
        c+=1
print("The number of vowels in string is: ",count)
print("The number of consonants in the string is: ",c)
