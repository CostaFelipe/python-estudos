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
