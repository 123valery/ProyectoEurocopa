from Ticket import Ticket

class VIP(Ticket):
    def __init__(self, seat, code,match,used):
        super().__init__(seat, code,match)
        self.price=75
        self.used=used