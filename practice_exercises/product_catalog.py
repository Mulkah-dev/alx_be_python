class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    
    def calculate_total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

product1 = Product("Apple", 200, 5 )
product2 = Product("Watermelon", 3000, 5)
product3 = Product("Pineapple", 1500, 4)

store = Store()
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

total_value = store.calculate_total_value()
print("Total value of products in stock:", total_value)
            