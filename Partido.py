
class Partido:
    def __init__(self,home,away,date,stadium,number, group):
        self.home=home
        self.away=away
        self.date=date
        self.stadium=stadium
        self.seats_vip=[]
        self.seats_gen=[]
        self.asistencia=[]
        self.number = number
        self.group = group
        
    def mostrar(self):

        return(f'''
        
    ---{self.home.name} VS {self.away.name}---

    Equipo local: {self.home.mostrar()}
    Equipo visitante: {self.away.mostrar()}
    Estadio: {self.stadium.mostrar()}
    Fecha: {self.date}
        
        ''')
    


    def resumen(self):
        '''muestra datos relevantes de un partido'''
        print(f'''----  {self.home.name} vs {self.away.name}  ----
                ''')
      