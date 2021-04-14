#coding=utf-8
#herança
#Definindo atributos e métodos da classe-filha
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank():
        print("This car need a gas tank!")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery_size(self):
        print(str(self.battery_size) + "-KWh battery")

my_tesla = ElectricCar('tesla', 'mode S', 2016)
my_tesla.describe_battery_size()

#Sobrescrevendo métodos da classe-pai
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery_size(self):
        print(str(self.battery_size) + "-KWh battery")
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'mode S', 2016)
my_tesla.fill_gas_tank()

#Instâncias como atributos
class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print(str(self.battery_size) + "-KWh batterys")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

#Instâncias como atributos II
class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print(str(self.battery_size) + "-KWh batterys")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Modelando objetos do mundo real
#FAÇA VOCÊ MESMO
#9.6 – Sorveteria
class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()
