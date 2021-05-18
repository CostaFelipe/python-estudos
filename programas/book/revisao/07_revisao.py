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

#verificando valores nas listas
motorcycles = ['ducati', 'honda', 'yamaha', 'bmw']
if "honda" in motorcycles:
    print(True)
else:
    print(False)

cars = ['bmw', 'audi']
cars_banned = ['ford', 'fiat', 'renault']
if cars not in cars_banned:
    print(cars)

#if else elif
age = 12
if age < 4: price = 0
elif age < 18: price = 5
else: price = 10

print(str(price))

#vericando lista vazia
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("add" + requested_topping)
        print("Finished make you pizza")
else:
    print("Are you sure you want a plain pizza?")

#dicionarios simples
alien_0 = {'color': "green", "points": 5}
print(alien_0)

#acessando dicionarios
print(alien_0['color'])
print(alien_0['points'])

#add novas chaves e valores
alien = {'color': 'orange', 'points': 10}
alien['position_x'] = 0
alien['position_y'] = 10
print(alien)

alien = {}
alien['color'] = 'yellow'
print(alien)

#deletando chaves-valor
del alien['color']
print(alien)

#pecorrendo dicionario using items()
user_0 = {'username': 'micke', 'first_name': 'Felipe',
          'last_name': 'Costa'}
#já treinando testes
if user_0:
    for key, value in user_0.items():
        print(key, value)
else:
    print("Não passou no teste")

#pecorrendo dicionario using keys()
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python'
                      }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print(name + " your favorite language is " +favorite_languages[name].title())

#exemplos usuarios items()
user_0 = {'username': 'micke', 'first_name': 'Felipe',
          'last_name': 'Costa'}
for key, value in user_0.items():
    print(key, value)

#favorite languages keys()
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      'raquel': 'c++',
                      'felipe': 'erlang',
                      'davi': 'haskell'
                      }
friends = ['felipe', 'sarah', 'davi']

for name in favorite_languages.keys():
    if name in friends:
        print(name, favorite_languages[name].title())

#values() dicionario
favorite_languages = {'felipe':'erlang', 'raquel':'c++', 'sarah':'c'}
for language in favorite_languages.values():
    print(language)

#sem repetições set()
favorite_languages = {'felipe':'c', 'raquel':'c++', 'sarah':'c'}
for language in set(favorite_languages.values()):
    print(language)

##informações aninhadas
alien_0 = {'color': 'yellow', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'orange','points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n")
#exemplo add, pecorrer, update
aliens = []
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#pecorrer
for alien in aliens:
    print(alien)

print("\n")

#update
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:10]:
    print(alien)

#mais exemplos
favorite_languages = {'felipe': ['erlang', 'elixir', 'python'],
                      'sarah': ['c', 'golang'], 'tim': ['python'],
                      'davi': ['hasckel', 'c++']}
for name, languages in favorite_languages.items():
    print(name.title())
    for language in languages:
        print("{" + language + "}")
