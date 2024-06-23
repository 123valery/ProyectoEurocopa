from Producto import Producto

class Alimento(Producto):
    tipo = 'alimento'
    def __init__(self, name, price, quantity, adicional):
        super().__init__(name, price, quantity)

        self.adicional = adicional
  
    def show(self):
        '''muestra la información del producto'''
        print(f"Tipo: {self.tipo}\nNombre: {self.name}\nPrecio :${self.price}\nPresentacion :{self.adicional}")