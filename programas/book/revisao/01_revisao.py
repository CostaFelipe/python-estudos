message = 'hello world'

print(message.upper())
print(message.lower())
print(message.title())
print(message.rstrip())
print(message.lstrip())
print(message.strip())

#concatenacao
message += " " + 'Brasil'
print(message)

#operacoes
print(1 + 1)
print(1.5 + 1)
print(2**2)
print(2 * 3)
print(10 / 5)
print(10 % 2)

#numbers favorite
number = 43
message = "My favorite number is" + " " + str(number)
print(message)

print("\n")
import this

#sustenido
print("\n")
#listas
bicycles = ['trek', 'cannonable', 'redline', 'sprecialized']
print(bicycles)

print(bicycles[-1].upper())
print(bicycles[0].lower())
print(bicycles[2].title())

#remover, add, subtituir listas
motocycles = ['honda', 'susaki']
motocycles[0] = 'ducati'
motocycles.append('honda')
print(motocycles)
