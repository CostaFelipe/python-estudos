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

#exercicios listas
#1)
names = ['Ruth', 'Levi', 'Sueli','Raimundo', 'Diego', 'Thiago', 'Nilson', 'Felipe']
print(names[0])
print(names[-1])
print(names[-2])
print(names[1])
print(names[2])
print(names[-3])
print(names[3])
print(names[-4])

#2)
message = "I love so much " + names[2] + "!"
print(message)

#3)
cars = ['bmw', 'troller', 'parati', 'citroen blue', 'Masserati']
message = "Gostaria de ter o carro " + cars[0].title() + "."
print(message)

#Modificando elementos de uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

#Acrescentando elementos em uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserindo elementos em uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removendo elementos de uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Removendo um item com o metodo pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

#Removendo um item de acordo com o valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('honda')
print(motorcycles)
