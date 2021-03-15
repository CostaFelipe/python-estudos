#coding=utf-8

cars = ['ford', 'toyota', 'fiat', 'subaru', 'bwm', 'jaguar']
print(cars)
car = cars[:]
print(car)

#lacos listas
for car in cars:
    print(car)

#lists comprehensions
testando = [car for car in cars]
print(testando)

#insert()
cars = ['ford', 'toyota', 'fiat', 'subaru', 'bwm', 'jaguar']
cars.insert(0,'merceds' )
print(cars)

#pop()
cars.pop()
print(cars)

#del nomelista[position]
del cars[0]
print(cars)

# .append("nome")
cars.append("hyndai")
print(cars)

#ordenando listas por ordem alfabetica use sort()
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#ordenando listas por ordem alfabetica use sorted() sem modificar a lista
#original
cars = ['ford', 'toyota', 'fiat', 'subaru', 'bwm', 'jaguar']
print("lista ordenada:" + str(sorted(cars)))
print("Não modificado mesmo usando sorte():", cars)

#reverse
cars.reverse()
print(cars)

#criando listas de números usando range()
numbers = list(range(10))
print(numbers)

#laços range()
for number in range(10):
    print(number)

#square
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#lists comprehensions exemplo
squares = [value**2 for value in range(1, 11)]
print("lists comprehensions:", squares)

#tuplas
dimensions = (10 , 100)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

#modificando tuplas
numbers = (100, 50)
print(numbers)
numbers = (200, 2)
for number in numbers:
    print(number)
print(numbers)

# if and else
age1 = 14
age2 = 12
if age1 == 14:
    print("verdade")
print(age1 <= 11 and age2 <= 12)
print(age1 <= 11 or age2 <= 12)

if age1 == 14 and age2 == 12:
    print("Verdade")
else:
    print("Falso")

if age1 == 11 and age2 == 12:
    print("Verdade")
else:
    print("Falso")

if age1 == 11 or age2 == 12:
    print("Verdade")
else:
    print("Falso")

if age1 >= 11 and age2 >= 12:
    print("Verdade")
else:
    print("Falso")
