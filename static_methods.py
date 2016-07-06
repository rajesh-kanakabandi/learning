

class A:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    @staticmethod
    def sum(a,b):
        return a + b

    def adder(self, a, b):
        return a + b

#
# class -> it a new type
#
# instance -> is an object of the type.
#
# i=9
# i is an instance of class int
#
# dog is an instance of Animal
#
# types of methods:
#
#     object method or instance method: owner = object. it has access to all the veriables and functions of the object
#     class method  : owner = class . used when building frameworks and libraries. can be accessed with the className or with the object.
#     static method : owner = class used when you want to build helper functions within the class with out access to the data of the objects
#
#
