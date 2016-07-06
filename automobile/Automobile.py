"""
	Name: Automobile.py
	Description: Base class for all Automobiles
"""

class Automobile:
    """
	base calss for all Automobiles
    """
    def __init__(self, auto_type, no_of_wheels = 2, purpose = "commute", period_between_services=2000):
        self.auto_type = auto_type
        self.no_of_wheels = no_of_wheels
        self.purpose = purpose
        self.miles = 0
        self.last_serviced_at = 0
        self.period_between_services = period_between_services

    def go(self, distance = 0):
        """ travels the number of miles specified"""
        self.miles += distance

    def service(self):
        """services the vehicle and sets the last serviced milage"""
        self.last_serviced_at = self.miles

    def get_info(self):
        return { 'type': self.auto_type,
                 'no_of_wheels': self.no_of_wheels,
                 'purpose': self.purpose,
                 'miles': self.miles,
                 'service_due_in': self.last_serviced_at + self.period_between_services - self.miles
                }

    def __str__(self):
        return "<Automobile type:{} miles: {} service in: {} >".format(self.auto_type, self.miles, self.last_serviced_at + self.period_between_services - self.miles) 
if __name__ == '__main__':
    bike = Automobile("bike")
    bike.go(1000)
    print(bike.get_info())
    print(bike)
