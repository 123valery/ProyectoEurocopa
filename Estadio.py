class Estadio:
    def __init__(self, stadium_id, name, city, capacity, restaurants):
        self.stadium_id = stadium_id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants
    
    def mostrar(self):

        return(f"Id: {self.stadium_id}\nName: {self.name}\nCapacity = {self.capacity}\nCapacity :{self.capacity}\n")
     
    
    def map (self, taken, i):
        asientos = self.capacity[i]

        for a in range(int(asientos/10)):
            fila = ["(x)" if f"{a}{b}" in taken else "( )" for b in range(10)]
            print(" ".join(fila))
    
