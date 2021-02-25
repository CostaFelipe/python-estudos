#listas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#acesso os elementos da listas
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[3].upper())
print(bicycles[2].lower())
print(bicycles[-1])
print(bicycles[-2])

#Usando valores individuais de uma lista
message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)
