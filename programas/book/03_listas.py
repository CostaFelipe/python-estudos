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
motocycles = ['honda', 'yamaha', 'suzuki']
motocycles[0] = 'ducati'
print(motocycles)

#Acrescentando elementos em uma lista
motocycles = ['honda', 'yamaha', 'suzuki']
motocycles.append('ducati')
print(motocycles)
