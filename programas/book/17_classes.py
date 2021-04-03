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
