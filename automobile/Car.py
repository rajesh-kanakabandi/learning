"""
	Name: Car.py
	Description: Car class
"""

from Automobile import Automobile

class Car(Automobile):
    """
	class for all cars
    """
    def __init__(self, period_between_services=3500):
        """
		Description: initializes an object of type car
		@param period_between_services: int
        """
        Automobile.__init__(self, "car",
                                 no_of_wheels = 4,
                                 period_between_services = period_between_services)


if __name__ == '__main__':
    car1 = Car(4000)
    car1.go(1000)
    print(car1.get_info())
    car1.go(3000)
    print(car1.get_info())



