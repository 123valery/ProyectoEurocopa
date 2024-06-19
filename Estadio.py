class Estadio:
    def __init__(self, id, name, city, capacity, restaurants):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants
    
    def mostrar(self):
        print(f"Id: {self.id}\nName: {self.name}\nCapacity = {self.capacity}\nRestaunrants: {self.restaurants}")
        for restaurant in self.restaurants:
            print(f'     {restaurant.name}')
    
