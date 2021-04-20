class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odemeter(self):
        print("this car " + str(self.odemeter_reading) + " miles on it.")
    def update_odemeter(self, mileage):
        if mileage >= self.odemeter_reading:
            self.odemeter_reading = mileage
        else:
            print("You can't rool back an odometer")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
