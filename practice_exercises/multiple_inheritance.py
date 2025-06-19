class Bird:
    def fly(self):
        return "flying"
    
class Mammal:
    def run(self):
        return "running"
    
class Bat(Bird,Mammal):
    def fly(self):
        return "Bat flying"
    
    def run(self):
        return "Bat running"
    
bat =Bat()
print(bat.fly())
print(bat.run())
