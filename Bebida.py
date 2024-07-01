from Producto import Producto

class Bebida(Producto):

    
    def __init__(self, name, price, stock, tipo, adicional):
        super().__init__(name, price, stock, tipo)

        self.adicional = adicional
  
    
    def mostrar(self):
        '''muestra la informacion del producto'''
        return f"\nName :{self.name}\nPrecio:{self.price}\nAdicional :{self.adicional}\nInventario :{self.stock}\n"