
class Partido:
    def __init__(self,home,away,date,stadium_id,match_id,number, group):
        self.home=home
        self.away=away
        self.date=date
        self.stadium_id=stadium_id
        self.match_id=match_id
        self.tickets_vip=[]
        self.tickets_gen=[]
        self.used=[]
        self.number = number
        self.group = group
        
    def mostrar(self):
        '''muestra la informacion de un partido'''
        return(f'''----  {self.home.name} vs {self.away.name}  ----
                    equipo local : {self.home.mostrar()}
                    equipo visitante: {self.away.mostrar()}
                    date: {self.date}
                    stadium: {self.stadium_id.mostrar()}
                    
                    
                ''')
    

    def resumen(self):
        '''muestra datos relevantes de un partido'''
        print(f'''----  {self.home.name} vs {self.away.name}  ----
                ''')
      