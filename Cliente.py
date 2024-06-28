class Cliente:
    def __init__(self, name, cedula, age):
        self.name = name
        self.cedula = cedula
        self.age = age
        self.tickets = []
    
    def mostrar_tickets(self):
        for ticket in self.tickets:
            print(ticket.mostrar())
    
    def mostrar_atrbiutos(self):
        return f''''
        Nombre :{self.name}
        Cedula: {self.cedula}
        Edad :{self.age}
        Tickets comprados : {len(self.tickets)}
        '''
