from Producto import Producto

class Alimento(Producto):
    
    def __init__(self, name, price, stock, tipo, adicional):
        super().__init__(name, price, stock, tipo)

        self.adicional = adicional
  
    
    def mostrar(self):
        '''muestra la informacion del producto'''
        return f"Name :{self.name}\nPrecio:{self.price}\nAdicional :{self.adicional}\n Inventario :{self.adicional}\n"