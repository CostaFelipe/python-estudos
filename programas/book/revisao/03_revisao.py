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
