class Equipo:
    def __init__(self, team_id, code, name, group):
        self.team_id = team_id
        self.code = code
        self.name = name
        self.group = group
    
    def mostrar(self):
        return(f"Id: {self.team_id}\nCode: {self.code}\nName: {self.name}\nGroup: {self.group}")