class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Person {self.name}, agem{self.age}, has been created")

    def __del__(self):
        print("f Person {self.name} has been deleted")