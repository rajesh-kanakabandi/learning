
class Employee:
    def __init__(self, name, salary, dep):
        self.name = name
        self.salary = salary
        self.dep = dep


    def who(self):
        print("I am {} from {}".format(self.name, self.dep))


class Sweeper(Employee):
    def __init__(self, name, salary, dep):
        Employee.__init__(self, name, salary, dep)
        self.does = "sweep"



# read about Inheritance, staticmethod classmethod, class variables,

# write a class Animal. eats = true
#write subclasses Herbivore, carnivore
            eats_meat = False

            eats_meat = True

# emp = Employee("John", 100000, 'IT')
#
# sw1 = Sweeper("Jack", 40000, "maint")
#
# sw1.does == "sweep"
