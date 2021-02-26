#primeiro
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

#Executando mais tarefas em um laco for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was great trick!")
    print("I can't wait to see the next trick" + magician.title() + "\n")
print("Thank you, everyone. That was a great magic show!")

#faca voce mesmo
pizzas = ['calabreza', 'portuguesa', 'pepperoni']
for pizza in pizzas:
    print("Gosto de pizza de " + pizza + ".")
print("Eu realmente gosto de pizzas!")

animals = ['cachorro', 'cavalo', 'elefante']
for animal in animals:
    print(animal)

for animal in animals:
    print("Um, " + animal.title() + " seria um otimo animal de estimacao")
print("Qualque um desses animais seria um otimo animal de estimacao")

#criando listas numericas range()
for number in range(1,5):
    print(number)

for value in range(10):
    print(value)

#Usando range() para criar uma lista de numeros
numbers = list(range(5))
print(numbers)

even_number = list(range(0,11,2))
print(even_number)

impar_number = list(range(1,22,2))
print(impar_number)

#quadrado perfeito

squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)

print("\n")

for value in range(1,11):
    squares.append(value ** 2)
    print(squares)

#Estatisticas simples com uma lista de numeros
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares = [value ** 2 for value in range(1,11)]
print(squares)

#exercicios
#1)
lista = range(1, 1000001)
print(min(lista))
print(max(lista))
print(sum(lista))

for value in range(1,20,2):
    print(value)

for value in range(3, 31):
    if value % 3 == 0:
        print(value)

cubos = []
for value in range(1,11):
    cubo = value ** 3
    cubos.append(cubo)
    print(cubos)

cubos = [value ** 3 for value in range(1, 11)]
print(cubos)
