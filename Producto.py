class Producto:
    def __init__(self, name, price, stock, tipo):
        self.name = name
        self.price = price
        self.stock = stock
        self.tipo = tipo
    
    def mostrar(self):
        return f'''
        
        Nombre: {self.name}
        Price : {self.price}
        Inventario : {self.stock}'
        '''