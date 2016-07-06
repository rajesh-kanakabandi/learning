

class Animal:
    breathes = True
    def __init__(self, walks=False, flys=False, crawls=False):
        """ Animal Object: base class for all Animals """
        self.is_human = False
        self.walks = walks
        self.flys = flys
        self.crawls = crawls
        self.__private_var = 10
        print("breathing : "+ str(Animal.breathes))

    def __private_method(self):
        print("Hello I'm Private")
        print (self.__private_var)
    def can_fly(self):
        self.__private_method()
        return self.flys
    def can_walk(self):
        return self.walks

    def set_flys(self, flys):
        self.flys = flys


    def set_walks(self):
        self.walks = walks
        Animal.fly()

    @classmethod
    def fly(my_class):
        print("I am a classmethod")

    @staticmethod
    def walk():
        print("I am a static method. I may walk ""




if __name__ == "__main__":
    dog = Animal(walks=True)
    dog.__private_var
    print("can fly " + str(dog.can_fly()))
