#revisao
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
