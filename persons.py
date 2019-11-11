class Person:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def cart_len(self):
        return len(self.cart)

    def add_to_cart(self , book):
        self.cart.insert(0, book)
        
    def pop_from_cart(self):
        return self.cart.pop()
    
class Woman(Person):
    pass

class Man(Person):
    pass
