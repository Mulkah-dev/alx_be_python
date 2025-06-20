class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def create_child(cls, name):
        return cls(name,0)
    
person1 = Person.create_child("Ayman")
print(person1.name)
print(person1.age)