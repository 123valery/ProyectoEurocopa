class Restaurant:
    def __init__(self, name , products) :
        self.name = name
        self.products = products

    
    def mostrar(self):
        print(f"Name:{self.name}\nProducts: {self.products}\n")