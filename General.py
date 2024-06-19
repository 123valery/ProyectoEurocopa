from Ticket import Ticket

class General(Ticket):
    def __init__(self, seat, code,match,used):
        super().__init__(seat, code,match)
        self.price=35
        self.used=used