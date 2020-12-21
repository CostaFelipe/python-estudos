"""
from math import *

#begin
print("Hello World")

#variables

character_name = "Esther"
character_age  = 30

print("There once was a man named", character_name)
print("She was", character_age, "years old.")

character_name = "Linda"
character_age  = "29"

print("She realy liked the name", character_name)
print("but didn't like being", character_age, ".")

#working with string

print(type("Ruth"))
print("Giraffe \n Academy")
print("Giraffe \" Academy \"")

phrase = "Giraffe Academy"
print(phrase)

print(phrase + " is cool")

print(phrase.lower())
print(phrase.upper())

print(phrase.upper().isupper())
print(phrase.islower())
print(len(phrase))

print(phrase[0])
print(phrase[:2])

print(phrase.index("i"))

print(phrase.replace("Giraffe", "Dog"))

#working with numbers
print(2)
print(2.7964)
print(-5)
print(2 + 5.99)
print(10 % 3)
print(10 // 3)

# math functions

my_number = -10
print(abs(my_number))

#expoente
print(pow(3,2))

print(max(10, 4))
print(min(2, 100))
print(round(5.10))

# import math

print(floor(3.7))
print(ceil(3.9))
print(sqrt(9))

"""

#getting input from users
#name = input("Enter your name: ")
#print("Hello,", name)

name = input("Enter your name:")
age  = input("Enter your age:")
print("Hello" +name+ "your age is", age, "years old.")