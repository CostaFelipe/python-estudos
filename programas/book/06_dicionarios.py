#dicionario simples
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#Acessando valores em um dicionario
print(alien_0['color'])
print(alien_0['points'])

print("\n")
#exemplo
alien = {'color': 'green', 'points': 10}
new_points = alien['points']
print("You just earned " + str(new_points) + " points!")

print("\n")
#Adicionando novos pares chave-valor
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n")
#Comecando com um dicionario vazio
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)

print("\n")
#Modificando valores em um dicionario
alien_1 = {'color': 'green'}
print("the alien is " + alien_1['color'])
alien_1['color'] = 'yellow'
print("the alien is now " + alien_1['color'])

print("\n")
alien_2 = {'x_positions': 0, 'y_positions': 25, 'speed': 'medium'}
if alien_2['speed'] == 'slow': x_positions = 1
elif alien_2['speed'] == 'medium': x_positions = 2
else: x_positions = 3

alien_2['x_positions'] = alien_2['x_positions'] + x_positions
print("o novo valor x_positions e: " + str(alien_2['x_positions']))

print("\nremovendo chave-valor")
#removendo chave-valor
alien = {'color': 'green', 'points': 5}
print(alien)
del alien['points']
print(alien)

print("\nUm dicionario de objetos semelhantes")
#Um dicionario de objetos semelhantes
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python'
                      }
print("Sarah favorite language is " +
       str(favorite_languages['sarah'].title()) +
      ".")

print("\nFaca voce mesmo")
#Faca voce mesmo
#6.1
people = {'first_name': 'sarah', 'last_name': 'costa',
          'age': 32, 'city': 'varsovia'}
print(people)

#6.2
favorite_numbers = {}
favorite_numbers['Felipe'] = 43
favorite_numbers['Sueli'] = 7
favorite_numbers['ruth'] = 30
favorite_numbers['raimundo'] = 17
favorite_numbers['levi'] = 21
print(favorite_numbers)

#6.3
glossario = {'lista': 'list', 'tupla': 'tuples', 'dicionario': 'dicionary'}
print(glossario['tupla'])

print("\nPercorrendo todos os pares com um laco")
#Percorrendo todos os pares chave-valor com um laco
user_0 = {'username': 'efermi', 'firts_name': 'enrico', 'last_name': 'fermi'}

for key, value in user_0.items():
    print(key + ": " + value)

print("\n")
favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python', }
for name, language in favorite_languages.items():
    print(name + " sua linguagem favorita e " + language)

#Percorrendo todas as chaves de um dicionario com um laco
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

print("\n")
favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python', }
friends = ['sarah', 'phil']
for name in favorite_languages.keys():
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

print("\nrevisando")
#revisando
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby',
                      'phil': 'pyhton'}
for name in favorite_languages.keys():
    print(name)

for name in favorite_languages:
    print(name.title())

print("\nrevisando")
favorite_language = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby',
                     'phil': 'python'}
friends = ['phil', 'sarah']
for name in favorite_language:
    if name in friends:
        print(name.title() + ", sua linguagem favorita e: " +
              favorite_language[name].title())

print("\nrevisando")
favorite_language = {'Felipe': 'erlang', 'sarah': 'c', 'peter': 'python',
                     'phil': 'python', 'edward': 'ruby'}
for languages in favorite_language.values():
    print(languages)

print("\nrevisando")

for languages in set(favorite_language.values()):
    print(languages)

print("\nFaca voce mesmo")
#faca voce mesmo
glossario = {'lista': 'list', 'tupla': 'tuples', 'dicionario': 'dicionary'}
glossario['for'] = 'laco'
glossario['if'] = 'condicional'
glossario['title()'] = 'primeira letra maiuscula'
glossario['upper()'] = 'todas letras maiuscula'
glossario['lower()'] = 'todas as letas minusculas'
for name, significado in glossario.items():
    print(name + ", significado e: " + significado)

print("\nFaca voce mesmo")
rios = {'egito': 'nilo', 'brasil':'amazonas', 'EUA': 'tennessee'}
for pais, rio in rios.items():
    print("O " + rio + " corre pelo " + pais.title())

#laco so c/ rios
for rio in rios.values():
    print(rio)

#laco so c/pais
for paises in rios.keys():
    print(paises.upper())

print("\nFaca voce mesmo")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby',
                      'phil': 'python', 'felipe': 'erlang', 'esther': 'elixir',
                      'levi': 'c++'}
friends = ['felipe', 'sarah', 'ruth', 'caio', 'jose']
for name in friends:
    if name in favorite_languages.keys():
        print("Ola " + name + ", obrigado por participar da enquente.")
    else:
        print("Ola " + name + ", voce deve participar da enquente.")

print("\nUma lista de dicionarios")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\nCriar lista de dicionarios")
aliens = []
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("total de alienigenas criados: " + str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

#Uma lista em um dicionario
print("\nUma lista em um dicionario")
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra-cheese']}
for topping in pizza['toppings']:
    print(topping)

print('\n')
favorite_languages = { 'jen': ['python', 'ruby'], 'sarah': ['c'],
                       'edward': ['ruby', 'go'],
                       'phil': ['python', 'haskell'], }
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite languages are:")
    for language in languages:
        print(language.title())

#lembrando
carros = []
for carro in range(5):
    novo_carro = {'color': 'preto', 'portas': 4, 'marca': 'ford', 'nome': 'KA'}
    carros.append(novo_carro)

for carro in carros:
    print(carro)
    
#Um dicionario em um dicionario
print('\nUm dicionario em um dicionario')
