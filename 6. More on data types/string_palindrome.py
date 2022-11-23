
'''
Check whether string entered by user is palindrome or not. (for a completely upper
case or a completely lower case, NO MIXED CASE)

            N I T I N
            -------->
            <--------

    if original string == reversed string  => It is palindrome
algo
===
step1:start
step2:reversed string entered by user.
step3:check reversed and original string
step4:if both are equal then its palindrome otherwise not.

reversed  ===>  [::-1]
'''

str1=input("Enter string: ")
rev_str=str1[::-1]
print("Original string: ",str1)
print("Original string: ",rev_str)

if str1==rev_str:
    print("It is a palindrome")

else:
    print("It is not a palindrome")
