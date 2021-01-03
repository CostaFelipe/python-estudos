#3. Write a Python program to get the largest number from a list.
numbers = [777, 443]
x = 1
maior = numbers[0]
while x < len(numbers):
   if numbers[x] > maior:
       maior = numbers[x]
   x+=1
print(maior)

