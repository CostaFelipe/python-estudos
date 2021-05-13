motocycles = ['honda', 'susuku', 'bmw']
motocycles.insert(0, 'ducati')
print(motocycles)

#deletar
del motocycles[0]
print(motocycles)

motocycles.remove('bmw')
print(motocycles)

#method pop
motocycles.pop()
print(motocycles)

var_remove = 'honda'
motocycles.remove(var_remove)
print(motocycles)

auto = ['ford', 'bmw', 'fiat', 'mercedes']
auto.sort()
print(auto)
auto = ['ford', 'bmw', 'fiat', 'mercedes']
print(sorted(auto))
auto.reverse()
print(auto)

magicians = ['alice', 'sakura', 'mrs. M']
for magician in magicians:
    print(magician)

for number in range(1, 11):
    print(number)

numbers = [number for number in range(1,11)]
print(numbers)

pesos_reciclagem = [87, 20]
total = 0
for peso in pesos_reciclagem:
    total = peso + total

print("Peso total da reciclagens:" + str(total) + "Kg")

for number in range(1, 11):
    print(number)
