import requests
import pickle
from Equipo import Equipo
from Partido import Partido
from Estadio import Estadio
from Restaurant import Restaurant
from Bebida import Bebida
from Alimento import Alimento
from Cliente import Cliente
from General import General
from VIP import VIP
from itertools import permutations


class App():

    def __init__(self):
        self.partidos = []
        self.equipos = []
        self.estadios = []
        self.clientes = []
        self.tickets = []


    def api_equipos(self):
        '''descarga la informacion del programa de la API en GitHub'''

        url_equipos = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'
        r_equipos = requests.get(url_equipos)
        info_equipos = r_equipos.json()
        return info_equipos
    

    def api_partidos(self):
        url_partidos = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'
        r_partidos = requests.get(url_partidos)
        info_partidos = r_partidos.json()
        return info_partidos
    
    def api_estadios(self):

        url_estadios = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
        r_estadios = requests.get(url_estadios)
        info_estadios = r_estadios.json()
        return info_estadios
    
    
    def comienzo(self):
        '''permite iniciar con la creacion de los objetos a partir de la api o del archivo txt creados '''
        print('\n---BIENVENIDO A LA VENTA DE TICKETS DE LA EUROCOPA DE FUTBOLA EURO2024---\n')
        load = input('Seleccione una opcion para la descarga de datos:\n1 - Reiniciciar programa \n2 -  Cargar datos anteriores\n=>')
        while not load.isnumeric() or int(load) !=1 and int(load) !=2:
            load = input('\nSeleccion invalida!\nSeleccione una opcion para la descarga de datos:\n1 - Reiniciciar programa \n2 -  Cargar datos anteriores\n=>')
        
        if int(load) ==1:
            self.create_obj()
            self.menu()

        if int(load)==2:
            try:
                self.estadios = pickle.load(open('Estadios.txt','rb'))
            except:
                self.estadios = list()
            
            try:
                self.equipos = pickle.load(open('Equipos.txt','rb'))
            except:
                self.equipos = list()
            
            try:
                self.partidos = pickle.load(open('Partidos.txt','rb'))
            except:
                self.partidos = list()
            
            try:
                self.clientes = pickle.load(open('Clientes.txt','rb'))
            except:
                self.clientes = list()
            
            try:
                self.tickets = pickle.load(open('Tickets.txt','rb'))
            except:
                self.tickets = list()

            self.menu()


    def menu(self):
        '''funcion menu que comienza el programa con la creaccion de los objetos a partir de la API o de los archovos txt'''

        while True:
            print('\n---BIENVENIDO A LA VENTA DE TICKETS DE LA EUROCOPA DE FUTBOLA EURO2024---\n')
            option=int(input('Para continuar seleccione una accion a realizar:\n1 - Buscar partidos\n2 - Registrar clientes\n3 - Comprar entradas\n4 -Confirmar Asistencia e\n5 - Buscar productos en Restaurantes\n6 - Mostrar Estadisticas\n7 - Salir y Guardar\n=> '))

            while not option.isnumeric() or (option!=1 and option!=2 and option!=3 and option!=4 and option!=5 and option!=6 and option!=7):
                option=int(input('Para continuar seleccione una accion a realizar:\n1 - Buscar partidos\n2 - Registrar clientes\n3 - Comprar entradas\n4 -Confirmar Asistencia e\n5 - Buscar productos en Restaurantes\n6 - Mostrar Estadisticas\n7 - Salir y Guardar\n=> '))
            
            '''opcion para buscar partidos por clasificacion'''
            if int(option) ==1:
                print('---- BIENVENIDO AL BUSCADOR DE PARTIDOS ----')
                search = input('\nComo desea busacr los partidos?\n1 - Pais\n2 - Estadios\n3 - Fecha \n=> ')
                while not search.isnumeric() or (int(search) != 1 and int(search) != 2 and int(search) != 3):
                    search = input('\nopcion invalida\nComo desea busacr los partidos?\n1 - Pais\n2 - Estadios\n3 - Fecha \n=> ')
                
                if int(search)==1:
                    self.search_by_country()
                elif int(search) ==2:
                    self.search_by_stadium()
                else:
                    self.search_by_date()
            #funcion para registrar cliente
            elif int(option)==2:
                self.register_client()

            #funcion para revisar clientes y hacer compra
            elif int(option) ==3:
                self.find_client()
            
            #confirmar asistencia al partido
            elif int(option) ==4:
                self.
            
            #compra y busqueda en el restaurante
            elif int(option) ==5:
                self.
            
            elif int(option)==6:
                self
            
            else:
                pickle.dump(self.estadios, open('Estadios.txt', 'wb'))
                pickle.dump(self.equipos, open('Equipos.txt', 'wb'))
                pickle.dump(self.partidos, open('Partidos.txt', 'wb'))
                pickle.dump(self.clientes, open('Clientes.txt', 'wb'))
                pickle.dump(self.tickets, open('Tickets.txt', 'wb'))

                print('\nguardando...\nListo!')
                break

    def create_obj(self):

        '''crea objetos para equipos, partidos y estadios a partir de la informacion de la API. Estos objetos se gaurdan en las listas '''
        
        partidos = self.api_partidos()
        equipos = self.api_equipos()
        estadios = self.api_estadios()

        #Equipos, creacion objetos
        for equipo in equipos:
            for key, value in equipo.items():

                equipo_actual = Equipo(equipo['id'],equipo['code'], equipo['name'], equipo['group'])

            self.equipos.append(equipo_actual)
        
        #ESTADIOS Y RESTAURANTES creacion de objetos
        for estadio in estadios:
            restaurantes = []
            for restaurant in estadio["restaurants"]:
                productos = []
                for productos in restaurant["products"]:
                    for key, value in productos.items():
                        name = productos["name"]
                        stock = int(productos["stock"])
                        price = float(productos["price"])
                        adicional = (productos["adicional"])
                    
                    if adicional == 'alcoholic' or adicional== 'non-alcoholic':
                        new_product = Bebida(name, price, stock, 'bebida', adicional)
                    
                    elif adicional == 'plate' or adicional== 'package':
                        new_product = Alimento(name, price, stock, 'alimento', adicional)
                    
                    productos.append(new_product)
                restaurante_actual = Restaurant(restaurant["name"], productos)
        
        #PARTIDOS creacion objetos
        for partido in partidos:
            for key, value in partido.items():
                for equipo in self.equipos:
                    home = partido["home"]["name"]
                    away = partido["home"]["name"]

                    if home == equipo.name:
                        home_actual = equipo
                    if away == equipo.name:
                        away_actual = equipo
                
                for estadio in self.estadios:
                    if partido ["stadium_id"]==estadio.stadium_id:
                        play_stadium = partido
                
                partido_actual = Equipo(partido["id"], partido["number"], home_actual, away_actual, partido["date"], partido["group"], play_stadium)
            self.partidos.append(partido_actual)


    def search_by_country(self):
        '''funcion de busqueda de partidos por pais'''
        print('---PAISES---')
        for i, equipo in enumerate(self.equipos):
            print(f"{i+1}. {equipo.name}")
        while True:
            try:
                country = input('Indique el pais para mostrar los partidos del equipo:  ').capitalize()
                found = False
                for equipo in self.equipos:
                    if country==equipo.name:
                        found = True
                        break
                if found == False:
                    raise Exception
                else:
                    break
            except:
                print('\nIngreso invalido! intente de nuevo\n')
        
        if found: 
            for partido in self.partidos:
                if partido.home.name == country:
                    print(partido.mostrar())
                if partido.away.name== country:
                    print(partido.mostrar())


    def search_by_stadium(self):
        '''funcion de busqueda de partidos segun estadio'''
        print('---ESTADIOS---')
        for estadio in self.estadios:
            print(f'''
            ID: {estadio.stadium_id}
            Estadio: {estadio.name}
                  ''')
        
        while True:
            try:
                stadium = int(input('Indique el id del estadio para mostrar los partidos del recinto:  '))
                found = False
                for estadio in self.estadios:
                    print(f"{estadio.stadium_id}= {stadium}")
                    if estadio.stadium_id==stadium:
                        found = True
                        break
                if found == False:
                    raise Exception
                else:
                    break
            except:
                print('\ningreso invalido! intente de nuevo\n')
        
        if found:
            for partido in self.partidos:
                if partido.stadium.stadium_id == stadium:
                    print(partido.mostrar())
        

    def search_by_date(self):
        '''funcion de busqueda de partidos segun fecha'''
        while True:
            try:
                found = False
                date = input('Ingrese la fecha del partido en el formato: aaaa-mm-dd \n>>')
                while date.isalpha():
                    date = input('Error. Ingrese la fecha del partido en el formato: aaaa-mm-dd \n>>')
                
                for partido in self.partidos:
                    if partido.date == date :
                        found = True
                        print(partido.mostrar())
                
                if found == False:
                    raise Exception
                else:
                    break
            except:
                print('\ningreso invalido! intente de nuevo\n')
    
    def register_client(self):
        '''registra la informacion de un nuevo cliente y la guarda en el programa como objeto Cliente'''
        print('\nAntes de continuar con la compra, debe registrarse en la base de datos')

        name = input('Ingrese su nombre:  ').capitalize()
        while not name.isalpha():
            name = input('\n Nombre invalido\nIngrese su nombre:  ').capitalize()
        
        
            cedula = input('Ingrese su numero de cedula:  ')
            while not cedula.isnumeric() or len(cedula)>8 or len(cedula)<7:
                cedula = input('Ingreso invalido. Ingrese su numero de cedula:  ')

            for client in self.clientes:
                if cedula == client.cedula:
                    print('la cedula ya se encuentra en la base de datos\n')
                    self.menu()

        while True:
            try:
                age = int(input('Ingrese su edad:  '))
                if age<9 or age>100:
                    raise Exception
                else:
                    break
            
            except:
                print('\nEsta seguro que esta es su edad? Intente de nuevo\n')
        
        cliente_actual = Cliente(name, cedula, age)
        self.clientes.append(cliente_actual)
        print("\nUsuario registrado exitosamente!\n")
        
      
    #objeto cliente
    def find_client(self):
        '''busca al cliente en la base de datos del programa'''
        cedula_cliente = input('Ingrese su numero de cedula:  ')
        while not cedula_cliente.isnumeric() or len(cedula_cliente)>8 or len(cedula_cliente)<7:
            cedula_cliente = input('Ingreso invalido. Ingrese su numero de cedula: ')
        
        for client in self.clientes:
                if cedula_cliente == client.cedula:
                    self.buy_ticket(cedula_cliente)
                    break
                else:
                    print('el usuario no se encuentra en la base de datos\n')
    

    def buy_ticket(self, cedula_cliente):

        cedula_cliente= input("Por favor ingrese la cedula del usuario: ")
        while not cedula_cliente.isnumeric() or len(cedula_cliente) > 9 or int(cedula_cliente) < 1:
            cedula_cliente = input("Ingreso invalido. Ingrese la cedula del usuario: ")
        
        for client in self.clients:
            if cedula_cliente == client.dni:

                ticket_id = (len(self.tickets)+1)

                for i, partido in enumerate(self.matches):
                    print(f"***{i+1}***\n")
                    print(partido.mostrar())

                seleccion = input("Ingrese el numero correspodiente al partido que desea atender\n >> ")
                while not seleccion.isnumeric() or int(seleccion) > len(self.partidos) or int(seleccion) < 1:
                    seleccion = input("Error. Ingrese el numero correspodiente al partido que desea atender\n >> ")
                
                partido = self.partidos[int(seleccion)-1]

                for client in self.clientes:
                    if cedula_cliente == client.dni:
                        for ticket in client.tickets:
                            if partido == ticket.match:
                                seleccion = input("Error. Usted ya compro una entrada para este partido: ")
                                partido = self.partidos[int(seleccion)-1]

                op_ticket = input("Ingrese 'G' para adquirir una entrada general o 'V' para adquirir una entrada VIP\n >> ").upper()
                while not op_ticket == 'G' and not op_ticket == 'V':
                    op_ticket = input("Error. Ingrese 'G' para adquirir una entrada general o 'V' para adquirir una entrada VIP\n >> ").upper()


                if op_ticket == "G":

                    descuento = 0
                    if self.es_vampiro(cedula_cliente):
                        descuento = 35/2

                    taken_seats = partido.seats_general

                    i = 0
                    partido.stadium.map(taken_seats, i)

                    chosen_seat = input("Ingrese el numero de asiento que desea\n >> ")
                    while not chosen_seat.isnumeric() or chosen_seat in taken_seats:
                        chosen_seat = input("Este asiento ya esta ocupado. Ingrese el numero de asiento que desea\n >>  ")

                    ticket = General(ticket_id, partido, chosen_seat, descuento)
                    print(ticket.mostrar())

                elif op_ticket == "V":

                    descuento = 0
                    if self.es_vampiro(cedula_cliente):
                        descuento = 75/2

                    taken_seats = partido.seats_vip
                    i = 1
                    partido.stadium.map(taken_seats, i)

                    chosen_seat = input("Ingrese el numero de asiento que desea\n >> ")
                    while not chosen_seat.isnumeric() or chosen_seat in taken_seats:
                        chosen_seat = input("Este asiento ya esta ocupado. Ingrese el numero de asiento que desea\n >> ")

                    ticket = VIP(ticket_id, partido, chosen_seat, descuento)
                    print(ticket.mostrar())
    
    def es_vampiro(self, cedula):
        '''calcula si la cedula de un cliente es un numero vampiro y regresa el descuento correspondiente'''
        try:
            if len(cedula) ==7:
                cedula = (f'0{cedula}')
            
            p = permutations(id, len(cedula))
            p_list = list(p)
            for n in p_list:
                joined = ''.join(n)
                x,y = joined[:int(len(joined)/2)], joined[int(len(joined)/2):]
                if x[-1]==0 and y[-1]==0:
                    continue
                if int(x)*int(y)==int(cedula):
                    return False
            
            return True
        except:
            return False
    
    def es_perfecto(self, cedula):
        '''calcula si el subtotal de una compra es un numero perfecto '''
        
        divisores = []
        for n in range(1, cedula):
            if cedula %n ==0:
                divisores.append(n)
        sum_divisores = sum(divisores)
        if sum_divisores == cedula:
            
            return True
        else:
            return False




    

                
      






