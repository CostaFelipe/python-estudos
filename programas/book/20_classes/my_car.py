from car import Car
from car import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odemeter_reading = 23
my_new_car.read_odemeter()
