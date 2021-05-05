import sys
import datetime
from math import pi

n = [1, 1, 1, 4]
soma = 0
for i in n:
    soma = soma + i
print(soma)

print("Twinkle, twinkle, little start, \n\t How I wonder what you are! \n\t\t Up abovethe world so high, \n\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are")


print("Python version")
print (sys.version)

now = datetime.datetime.now()
print(now)

r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
