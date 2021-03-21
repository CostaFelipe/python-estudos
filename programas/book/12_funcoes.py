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
