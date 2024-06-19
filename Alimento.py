from Producto import Producto

class Alimento(Producto):
    def __init__(self, name, price, quantity, adicional, type):
        super().__init__(name, price, quantity)

        self.adicional = adicional
        self.type = type
    
    def show(self):
        '''muestra la información del producto'''
        print(f"Nombre: {self.nombre}\nPrecio :${self.price}\nPresentacion :{self.adicional}")