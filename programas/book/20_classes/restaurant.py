class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " " + self.cuisine_type)
    def open_restaurant():
        print("O restaurante esta aberto")
    def set_number_served(self, set_number):
        self.number_served = set_number
    def increment_number_served(self, count):
        self.number_served += count
    def read_number_served(self):
        print("Pessoas atendidas: " + str(self.number_served))
