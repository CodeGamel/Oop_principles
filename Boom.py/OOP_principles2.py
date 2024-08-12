from OOP_principles import d

class Product:
    
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name 
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

class Book(Product):
    
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)  
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
        
class Computer(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)  
        self.specs = specs

    def display_info(self):
        super().display_info
        print(f"Product ID: {self.product_id}")
        print(f"Specs: {self.specs}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

class Clothes(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)  
        self.size = size

    def display_info(self):
        super().display_info
        print(f"Product ID: {self.product_id}")
        print(f"Sizes : {self.size}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()
d()
my_computer = Computer("420", "The Mid", 999.99, "Intel I7 4770k/ RTX 2060/ 16gb Ram/ 500 SSD M.2 Drive")
my_computer.display_info()
d()
my_drip = Clothes("6969", "Light-Up Sketchers Shoes", 99.99, "11 mens")
my_drip.display_info()

