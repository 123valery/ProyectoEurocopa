from Producto import Producto

class Bebida(Producto):
    def __init__(self, name, price, quantity, adicional, type):
        super().__init__(name, price, quantity)

        self.adicional = adicional
        self.type = type
    
    def show(self):
        '''muestra la informacion del producto'''
        print(f"Name :{self.name}\nPrecio:{self.price}\n")