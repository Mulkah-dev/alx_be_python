class Shape:
    def calculate_area(self):
        return 0
    
class Rectangle(Shape):
    def calculate_area(self,length,breadth):
        self.length = length
        self.breadth = breadth
        return length * breadth
    
rectangle = Rectangle()
print(rectangle.calculate_area(4,5))
    
