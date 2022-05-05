#write a program to generate OTP 
import math
import random

#function to generate OTP
def generateOTP():
    #declare a Digits variable 
    #which stores all digits
    digits = '0123456789'
    OTP =""

    #length of password can be changed
    #by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10 )]

    return OTP

if __name__ == "__main__":
    print("OTP of 4 digits : ",generateOTP())