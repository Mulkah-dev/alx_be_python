class Animal:
    def __init__(self, name):
        self.name = name
       
    def eat(self):
        print(f"{self.name} eats bone")

    def sleep(self):
        print(f"{self.name} sleeps in its assigned place")

class Dog(Animal):
    def eat(self):
        print(f"{self.name} eats bone")

    def sleep(self):
        print(f"{self.name} sleeps in its assigned place")

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Lucky")
dog1.eat()
dog1.sleep()
dog1.bark()