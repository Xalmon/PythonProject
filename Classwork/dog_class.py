from Classwork.exception_class import DogException


class Animal:
    def __init__(self):
        self.number_of_nose = 1

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        self.number_of_legs = 4
        super.__init__()

    @property
    def number_of_legs(self):
        return self.number_of_legs

    @number_of_legs.setter
    def number_of_legs(self):
        if value != 4:
            raise DogException("Invalid numbers of legs")

    def walk(self):
        print(f"walking with {self.number_of_legs}")


class Fish(Animal):
    def swim(self):
        print("swimming")


fish1 = Fish()

fish1.eat()
