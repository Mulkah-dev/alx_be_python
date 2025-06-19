class Dog:
    def make_sound(self):
        return "woof!"
    
class Cat:
    def make_sound(self):
        return "meow!"
    
class Bird:
    def make_sound(self):
        return "skrr"
    
def let_them_speak(animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()
bird = Bird()

print(let_them_speak(dog))
print(let_them_speak(cat))
print(let_them_speak(bird))
    
    
