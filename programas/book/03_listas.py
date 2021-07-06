#listas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

languages = ['elixir', 'golang', 'python', 'erlang', 'typescript']
print(languages)

cars = ['jepp', 'offroads', 'luxe', 'prime']

#acesso os elementos da listas
print(cars[1])
print(cars[2].lower())
print(cars[3].upper())
print(cars[0].title())

print(languages[1])
print(languages[2].title())
print(languages[3].upper())
print(languages[4].lower())

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[3].upper())
print(bicycles[2].lower())
print(bicycles[-1])
print(bicycles[-2])

#Usando valores individuais de uma lista
message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)

message = "my cars favorite were a " + cars[1].title() + "."
print(message)

framework = "Phoenix is framework for " + languages[1].title() + "."
print(framework)

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

cars_brands = ['jaguar', 'ford', 'toyota', 'honda', 'bmw']
cars_brands[0] = 'fiat'
print(cars_brands)

languages = ['elixir', 'golang', 'python']
languages[1] = 'typescript'
print(languages)

#Acrescentando elementos em uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

languages = ['elixir', 'golang', 'python']
languages.append('scala')
print(languages)


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

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

#Ordenando uma lista de forma permanente com o metodo sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

numbers = [9, 5, 8, 4]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#Ordenando uma lista temporariamente com a funcao sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print(cars)

print("Here is the original list:")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("Here is the sort list:")
cars.sort()
print(cars)

#Exibindo uma lista em ordem inversa
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#Descobrindo o tamanho de uma lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#exercicios
#1)
citys = ['tokio', 'Santa Catarina', 'Jerusalem', 'Manila', 'Rio Branco']
print("Ordem original:", citys)
print(sorted(citys))
print(citys)
citys.reverse()
print(citys)
citys.reverse()
print(citys)
citys.sort()
print(citys)
citys.sort(reverse=True)
print(citys)
#2)
convidados = [1, 2, 3, 4, 5, 8, 33, 100]
print(len(convidados))

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

print("Soma total da lista:", sum_list([1,2,-8]))
