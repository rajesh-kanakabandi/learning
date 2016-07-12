import sys
sys.path.append('/Users/rajesh/Documents/dev/learning/automobile')
from Car import Car

class Fleet:
    def __init__(self):
        self.cars = []
        self.rented_cars = []
        self.available_cars = 0

    def get_status(self):
        return "{} of {} rented. {} cars available".format(len(self.rented_cars), len(self.cars) + len(self.rented_cars), self.available_cars)

    def add_car(self, car):
        self.cars.append(Car())
        self.available_cars += 1
        return "new Car in fleet"

    def rent_car(self):
        if self.available_cars > 0:
            self.rented_cars.append(self.cars.pop())
            self.available_cars -= 1
            return "Successfully Rented a car"
        else:
            return "No Cars Available to rent."

    def return_car(self):
        self.cars.append(self.rented_cars.pop())
        self.available_cars += 1
        return "One car back to the fleet"
