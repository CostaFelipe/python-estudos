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

even_number = list(range(2,11,2))
print(even_number)
