#Random module

import random as r

#random()
x=r.random()#fraction value between 0-1
print(x)

#OTP generation.

t=x*10000
print(t)

otp=round(t)
print("Otp=",otp)

#This can also be written as

otp2=round(r.random()*10000)
print("OTP is=",otp2)
