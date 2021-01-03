#Write a Python program to sum all the items in a list. 
items = [2, 3, 5]
soma = 0
x = 0
while x < len(items):
    soma = soma + items[x]
    x+=1
print(soma) 