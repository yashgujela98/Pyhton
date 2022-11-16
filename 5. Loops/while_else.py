'''
while...else
===========

syntax:

initialization

while condition:

    body of while loop

    increment/decrement

else:
    else part of while loop

    
for...else
==========

for var in range(start,stop,step):

    body of for loop

else:

   else part of for loop


else part is executed when loop condition become false or loop terminate

'''


for i in range(1,5,1):
    if i==3:
        break
    
    print("In for loop")

else:
    print("In else part of loop")
