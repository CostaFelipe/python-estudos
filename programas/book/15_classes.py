#coding=utf-8
#classes
#Criando e usando uma classe
class Dog():
    """Uma tentativa simples de modelar uma classe"""
    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def rool_over(self):
        print(self.name.title() + " rolled over!")

#Criando uma instância a partir de uma classe
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#Chamando métodos
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.rool_over()

#Criando várias instâncias
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is "+ str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


#fazendo outra classe
class Auto():
    def __init__(self, marca, nome):
        self.marca = marca
        self.nome = nome
    def show(self):
        print("Essa é a marca:" + self.marca.title() + " com nome " + self.nome)

auto = Auto("ford", "F500")
auto.show()

#Acessando atributos
print(auto.marca.title() + " " + auto.nome.title())

#Chamando métodos
my_dog = Dog('willie', 6)
my_dog.sit()

#Criando várias instâncias
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is "+ str(my_dog.age) + " years old.")
my_dog.sit()


#FAÇA VOCÊ MESMO
#9.1 – Restaurante
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " " + self.cuisine_type)
    def open_restaurant():
        print("O restaurante está aberto")


restaurant = Restaurant('Robert', 'classic')
print(restaurant.restaurant_name.title() + " tipo :" + restaurant.cuisine_type)
restaurant.describe_restaurant()

#9.2 – Três restaurantes
restaurant_01 = Restaurant('Robert', 'classic')
restaurant_02 = Restaurant('felipe', 'nordeste')
restaurant_03 = Restaurant('joice', 'tite')

restaurant_01.describe_restaurant()
restaurant_02.describe_restaurant()
restaurant_03.describe_restaurant()

#9.3 – Usuários
class User():
    def __init__(self, first_name, last_name, age, email, status=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.status = status
    def describe_user(self):
        print("O usuario " + self.last_name.title() + " possui o email:" + self.email)
    def greet_user(self):
        print("Olá, " + self.first_name.title() + " " + self.last_name)

user01 = User('Felipe', 'Costa', 32, 'costa@gmail.com')
user02 = User('Esther', 'Costa', 31, 'esther@gmail.com')
user03 = User('Linda', 'Gomes', 28, 'linda@gmail.com')

user01.describe_user()
user02.describe_user()
user03.describe_user()

user01.greet_user()
user02.greet_user()
user03.greet_user()
