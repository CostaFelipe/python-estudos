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

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery_size(self):
        print(str(self.battery_size) + "-KWh battery")

my_tesla = ElectricCar('tesla', 'mode S', 2016)
my_tesla.describe_battery_size()
