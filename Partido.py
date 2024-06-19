
class Partido:
    def __init__(self,home_team,away_team,date,stadium_id,id,tickets_sold,tickets_used,number):
        self.home_team=home_team
        self.away_team=away_team
        self.date=date
        self.stadium_id=stadium_id
        self.id=id
        self.tickets_sold=tickets_sold
        self.used=tickets_used
        self.number = number
        
    def show(self):
        '''muestra la informacion de un partido'''
        print(f'''----  {self.home_team.name} vs {self.away_team.name}  ----
                    date: {self.date}
                    stadium: {self.stadium_id.name})
                    date: {self.date}')
                    stadium: {self.stadium_id.name}
                    id: {self.id}
                    number : {self.number}''')
    

    def show_stats(self):
        '''muestra datos relevantes de un partido'''
        print(f'''----  {self.home_team.name} vs {self.away_team.name}  ----
                    stadium: {self.stadium_id.name}
                    tickets vendidos: {self.tickets_sold}''')
      