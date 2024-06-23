from Producto import Producto

class Bebida(Producto):

    tipo = 'bebida'
    def __init__(self, name, price, quantity, adicional):
        super().__init__(name, price, quantity)

        self.adicional = adicional
  
    
    def show(self):
        '''muestra la informacion del producto'''
        print(f"Tipo : {self.tipo}\nName :{self.name}\nPrecio:{self.price}\nTipo de bebida :{self.adicional}")