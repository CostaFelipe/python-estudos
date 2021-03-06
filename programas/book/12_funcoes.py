#coding=utf-8
#Usando um laço while com listas e dicionários
def greet_user():
    print("hello")

greet_user()

#Passando informações para uma função
def greet_user(username):
    """Exibe uma mensagem simples """
    print("Hello " + username)

greet_user('Felipe')

#Argumentos e parâmetros
#'Felipe' é o argumento e os parâmentro username

#FAÇA VOCÊ MESMO
#8.1 – Mensagem
def display_message():
    print("Estamos aprendendo sobre funções, parâmentros e argumentos")

display_message()

#8.2 – Livro favorito
def favorite_book(title):
    print("Um dos meus livros favoritos é, " + title)

favorite_book("A VIDA INTELECTUAL de A. D. SERTILLANGES ")

#Passando argumentos
#Argumentos posicionais
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('dog', 'aika')

#Várias chamadas de função
describe_pet('cat', 'naninha')
describe_pet('dog', 'mishuki')

#A ordem é importante em argumentos posicionais
def book(author, title):
    print("\nMy favorite book is " + title + ":" + author)
book('A VIDA INTELECTUAL', 'A. D. SERTILLANGES')

#Argumentos nomeados
def describe_pets(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pets(animal_type = 'dog', pet_name = 'aika')

#Valores default
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='aika')

#Chamadas de função equivalentes
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#Evitando erros em argumentos
"""
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet()

File "pets.py", line 6, in <module> v
describe_pet() w TypeError: describe_pet() missing 2 required
positional arguments: 'animal_
type' and 'pet_name'
"""

#FAÇA VOCÊ MESMO
#8.3 – Camiseta:
def make_shirt(tamanho, message_shirt):
    print("\nO tamanho da camisa é " + tamanho + "\na frase a ser estampada deve ser:"
         + message_shirt)
make_shirt('GG', 'Amor, fé e esperança')
make_shirt(tamanho='G', message_shirt='Deus é meu protetor')

#8.4 – Camisetas grandes
def make_shirt(message_shirt, tamanho='G'):
    print("\nO tamanho da camisa é " + tamanho + "\na frase a ser estampada deve ser:"
         + message_shirt)

make_shirt(message_shirt='morrer em Cristo é viver em cristo')
make_shirt(message_shirt='Cristo é Rei', tamanho='PP')

#8.5 – Cidades
def describe_city(city, country='Brazil'):
    print(city.title() + " está localizada n(o)a " + country )

describe_city(city='fortaleza')
describe_city(city='Reyjavik', country='Islândia')
describe_city(country='EUA', city='Boston')

#Valores de retorno
#Devolvendo um valor simples
def get_formatted_name(firstname, lastname):
    full_name = firstname + ' ' + lastname
    return full_name.title()

name = get_formatted_name('Felipe', 'Costa')
print(name)

#Deixando um argumento opcional
def get_formatted_name(firstname, middlename, lastname):
    full_name = firstname + ' ' + middlename + ' ' + lastname
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#mesma função
def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)

#Devolvendo um dicionário
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

#exemplo
def build_person(first_name, last_name, age=""):
    person = {'first': first_name,'last': last_name}
    if age:
        person['age'] = age
        return person
    else:
        return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
musician = build_person('jimi', 'hendrix')
print(musician)

#Usando uma função com um laço while
"""
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("Primeiro nome: ")
    l_name = input("Last name: ")
formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")
"""

#usando estrutura break + function + while
"""
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\n Por favor me diga seu nome:")
    print("(enter 'q' at any time to quit)")
    f_name = input("Digite seu primeiro nome:")
    l_name = input("Digite seu sobrenome:")
    if f_name == 'quit': break
    if l_name == 'quit': break
    else: print("\nVamos continuar então")
formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")
"""

#FAÇA VOCÊ MESMO
#8.6 – Nomes de cidade
def city_country(city, country):
    print(city.title() + ", " + country.title())
city_country('fortaleza', 'brasil')
city_country('santa catarina', 'brasil')
city_country('são paulo', 'brasil')

#8.7 – Álbum
def make_album(singer, title_album, faixa=""):
    if faixa:
        album = {'cantor': singer, 'title': title_album, 'faixas': faixa}
        return album
    else:
        album = {'cantor': singer, 'title': title_album}
        return album
musician01 = make_album('ciro nogueira', 'senhor')
musician02 = make_album('chico nogueira', 'vale a pena')
musician03 = make_album('chico', 'chiquinho')
musician04 = make_album('ciro nogueira', 'senhor', 32)
print(musician01, musician02, musician03, musician04)

#8.8 – Álbuns dos usuários
"""
def make_album(cantor, titulo_do_album):
    album = cantor + ", " + titulo_do_album
    return album

while True:
    print("\nAdd o cantor e album e para sair digite 'sair'")
    artista = input("Add o nome do cantor:")
    album = input("Add o titulo do album:")
    if artista == "sair": break
    if album == "sair": break
formatted_artist = make_album(artista, album)
print("\nHello, " + formatted_artist + "!")
"""

#Passando uma lista para uma função
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
