#coding=utf-8
#classes
#FAÇA VOCÊ MESMO

#9.4 – Pessoas atendidas
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " " + self.cuisine_type)
    def open_restaurant():
        print("O restaurante está aberto")
    def set_number_served(self, set_number):
        self.number_served = set_number
    def increment_number_served(self, count):
        self.number_served += count
    def read_number_served(self):
        print("Pessoas atendidas: " + str(self.number_served))

restaurant = Restaurant("Indiano", "indiana")
restaurant.set_number_served(5)
restaurant.read_number_served()
restaurant.set_number_served(8)
restaurant.read_number_served()
restaurant.increment_number_served(2)
restaurant.read_number_served()

#9.5 – Tentativas de login
class User():
    def __init__(self, first_name, last_name, age, email, status=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.status = status
        self.login_attempts = 0
    def describe_user(self):
        print("O usuario " + self.last_name.title() + " possui o email:" + self.email)
    def greet_user(self):
        print("Olá, " + self.first_name.title() + " " + self.last_name)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def read_login_attempts(self):
        print("Loggs:" + str(self.login_attempts))

user = User('Felipe', 'lima', 15, 'lima@gmail.com')
user.increment_login_attempts()
user.read_login_attempts()
user.increment_login_attempts()
user.read_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()
