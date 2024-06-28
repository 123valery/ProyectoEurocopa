class Restaurant:
    def __init__(self, name , products) :
        self.name = name
        self.products = products


    def mostrar_productos(self):
        for producto in self.products:
            print(producto.mostrar())
    
    def mostrar(self):
        print(f"\nName:{self.name}\nProducts: \n")
        self.mostrar_productos()