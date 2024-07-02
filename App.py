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
from Factura import Factura


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
        load = input('Seleccione una opcion para la descarga de datos:\n1 - Reiniciciar programa \n2 - Cargar datos anteriores\n=>')
        while not load.isnumeric() or int(load) <1 and int(load) >2:
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
            print('\n---BIENVENIDO A LA EUROCOPA DE FUTBOLA EURO2024---\n')
            option=input('Para continuar seleccione una accion a realizar:\n1 - Buscar partidos\n2 - Registrar clientes\n3 - Comprar entradas\n4 - Confirmar Asistencia \n5 - Restaurantes\n6 - Mostrar Estadisticas\n7 - Salir y Guardar\n=> ')

            while not option.isnumeric() or int(option) <1 or int(option) >7:
                option=input('Para continuar seleccione una accion a realizar:\n1 - Buscar partidos\n2 - Registrar clientes\n3 - Comprar entradas\n4 -Confirmar Asistencia e\n5 - Buscar productos en Restaurantes\n6 - Mostrar Estadisticas\n7 - Salir y Guardar\n=> ')
            
            '''opcion para buscar partidos por clasificacion'''
            if int(option) ==1:
                print('---- BIENVENIDO AL BUSCADOR DE PARTIDOS ----')
                search = input('\nComo desea busacr los partidos?\n1 - Pais\n2 - Estadios\n3 - Fecha \n=> ')
                while not search.isnumeric() or int(search) < 1 or int(search) >7:
                    search = input('\nopcion invalida\nComo desea busacr los partidos?\n1 - Pais\n2 - Estadios\n3 - Fecha \n=> ')
                
                if int(search)==1:
                    self.search_by_country()
                elif int(search) ==2:
                    self.search_by_stadium()
                elif int(search)==3:
                    self.search_by_date()
            #funcion para registrar cliente
            elif int(option)==2:
                self.register_client()

            #funcion para revisar clientes y hacer compra
            elif int(option) ==3:
                self.find_client()
            
            #confirmar asistencia al partido
            elif int(option) ==4:
                self.asistencia()
            
            #compra y busqueda en el restaurante
            elif int(option) ==5:
                self.manage_rest()
            
            elif int(option)==6:
                self.estadisticas()
            
            elif int(option)==7:
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
                for products in restaurant["products"]:
                    for key, value in products.items():
                        name = products["name"]
                        stock = int(products["stock"])
                        price = float(products["price"])
                        adicional = products["adicional"]
                    
                    if adicional == 'alcoholic' or adicional== 'non-alcoholic':
                        new_product = Bebida(name, price, stock, 'bebida', adicional)
                    
                    elif adicional == 'plate' or adicional== 'package':
                        new_product = Alimento(name, price, stock, 'alimento', adicional)
                    
                    productos.append(new_product)
                restaurante_actual = Restaurant(restaurant["name"], productos)
                restaurantes.append(restaurante_actual)

                estadio_actual = Estadio(estadio["id"],  estadio["name"], estadio["city"], estadio["capacity"], restaurantes)
            self.estadios.append(estadio_actual)
        
        #se crean los  objetos tipo partido
        for partido in partidos:
            for key, value in partido.items():
                for equipo in self.equipos:
                    home = partido["home"]["name"]
                    away = partido["away"]["name"]

                    if home == equipo.name:
                        home_actual = equipo
                    if away == equipo.name:
                        away_actual = equipo
                
                for estadio in self.estadios:
                    if partido ["stadium_id"]==estadio.stadium_id:
                        play_stadium = estadio
                
                partido_actual = Partido(home_actual, away_actual,partido["date"],play_stadium, partido["number"], partido["group"])
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
                stadium = input('Indique el id del estadio para mostrar los partidos del recinto:  ')
                
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
        while name.isnumeric():
            name = input('\n Nombre invalido\nIngrese su nombre:  ').capitalize()
        
        
        cedula = input('Ingrese su numero de cedula:  ')
        while not cedula.isnumeric() or len(cedula)>9 or len(cedula)<1:
            cedula = input('Ingreso invalido. Ingrese su numero de cedula:  ')

        for client in self.clientes:
            if cedula == client.cedula:
                print('la cedula ya se encuentra en la base de datos\n')
                self.menu()

        age = input("Ingrese la edad:   ")
        while not age.isnumeric() or int(age) > 100 or int(age)<1:
            age = input("Ingreso invalido. Ingrese la edad:   ")

        
        cliente_actual = Cliente(name, cedula, age)
        self.clientes.append(cliente_actual)
        print("\nUsuario registrado exitosamente!\n")
        
      
    #objeto cliente
    def find_client(self):
        '''busca al cliente en la base de datos del programa'''
        cedula_cliente = input('Ingrese su numero de cedula:  ')
        while not cedula_cliente.isnumeric() or len(cedula_cliente)>9 or len(cedula_cliente)<1:
            cedula_cliente = input('Ingreso invalido. Ingrese su numero de cedula: ')
        
        for client in self.clientes:
            if cedula_cliente == client.cedula:
                self.buy_ticket(cedula_cliente)
                break
            else:
                print('el usuario no se encuentra en la base de datos\n')
    
    #funcion para comprar tickets
    def buy_ticket(self, cedula_cliente):

        while not cedula_cliente.isnumeric() or len(cedula_cliente) > 9 or int(cedula_cliente) < 1:
            cedula_cliente = input("Ingreso invalido. Ingrese la cedula del usuario: ")
        
        for client in self.clientes:
            if cedula_cliente == client.cedula:

                ticket_id = (len(self.tickets)+1)

                for i, match in enumerate(self.partidos):
                    print(f"***{i+1}***\n")
                    print(match.mostrar())

                seleccion = input("Ingrese el numero correspodiente al partido que desea atender\n >> ")
                while not seleccion.isnumeric() or int(seleccion) > len(self.partidos) or int(seleccion) < 1:
                    seleccion = input("Error. Ingrese el numero correspodiente al partido que desea atender\n >> ")
                
                match = self.partidos[int(seleccion)-1]

                for client in self.clientes:
                    if cedula_cliente == client.cedula:
                        for ticket in client.tickets:
                            if match == ticket.match:
                                seleccion = input("Error. Usted ya compro una entrada para este partido: ")
                                match = self.partidos[int(seleccion)-1]

                op_ticket = input("Ingrese 'G' para adquirir una entrada general o 'V' para adquirir una entrada VIP\n >> ").upper()
                while not op_ticket == 'G' and not op_ticket == 'V':
                    op_ticket = input("Error. Ingrese 'G' para adquirir una entrada general o 'V' para adquirir una entrada VIP\n >> ").upper()


                if op_ticket == "G":

                    descuento = 0
                    if self.es_vampiro(cedula_cliente):
                        descuento = 35/2

                    taken_seats = match.seats_gen

                    i = 0
                    match.stadium.map(taken_seats, i)

                    chosen_seat = input("Ingrese el numero de asiento que desea\n >> ")
                    while not chosen_seat.isnumeric() or chosen_seat in taken_seats:
                        chosen_seat = input("Este asiento ya esta ocupado. Ingrese el numero de asiento que desea\n >>  ")

                    ticket = General(ticket_id, match, chosen_seat, descuento)
                    print(ticket.mostrar())

                elif op_ticket == "V":

                    descuento = 0
                    if self.es_vampiro(cedula_cliente):
                        descuento = 75/2

                    taken_seats = match.seats_vip
                    i = 1
                    match.stadium.map(taken_seats, i)

                    chosen_seat = input("Ingrese el numero de asiento que desea\n >> ")
                    while not chosen_seat.isnumeric() or chosen_seat in taken_seats:
                        chosen_seat = input("Este asiento ya esta ocupado. Ingrese el numero de asiento que desea\n >> ")

                    ticket = VIP(ticket_id, match, chosen_seat, descuento)
                    print(ticket.mostrar())

                #confirmacion de la compra 
                opcion = input("Desea continuar con la compra de entradas?\n1. Si\n2. No\n")
                while not opcion.isnumeric() or (int(opcion)!= 1 and int(opcion)!= 2):
                    opcion = input("Ingreso invalido.Desea continuar con la compra de entradas?\n1. Si\n2. No\n")
                
                if int(opcion)==1:
                    self.tickets.append(ticket)

                    if isinstance(ticket, General):
                        print(chosen_seat)
                        match.seats_gen.append(chosen_seat)
                    elif isinstance(ticket, VIP):
                        match.seats_vip.append(chosen_seat)
                
                    for client in self.clientes:
                        if cedula_cliente == client.cedula:
                            client.tickets.append(ticket)
                            print(client.mostrar_atributos())
                        
                    print("Su compra ha sido procesada exitosamente!")
        
                else:
                    print("Su compra no fue finaliada!")
                    self.menu




    
    def es_vampiro(self, id):
        vampiro = False
        
        if len(str(id)) %2 !=0:
            return 0
        else:
            p=permutations(str(id),len(str(id)))
            p_list=list(p)
            for n in p_list:
                joined=''.join(n)
                x,y=joined[:int(len(joined)/2)],joined[int(len(joined)/2):]
                if x[-1]==0 and y[-1]==0:
                    continue
                if int(x)*int(y)==int(id):
                    vampiro=True
        
        if vampiro==False:
            return 0
        else:
            return True
    
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
    
    def asistencia(self):
        found = False

        ticket_id = input("Ingrese el ticket ID: ")
        while not found:
            for ticket in self.tickets:
                if int(ticket_id) == int(ticket.ticket_id):
                    found = True
                    if not ticket_id in ticket.match.asistencia:
                        print("Usted esta dentro del estadio")
                        ticket.match.asistencia.append(ticket_id)
                        break
                    else:
                        print("Ingreso invalido. Este ticket ya fue empleado para el ingreso al partido\n ")
            
            if not found:
                print("Error. El ticket ID no se ha encontrado")
                break



    #restaurante
    def manage_rest(self):
        print(f'''
        1. Buscar productos
        2. Comprar productos
        ''')
        
        selec_rest = input('Ingrese una opcion valida: ')
        while not selec_rest.isnumeric() or (int(selec_rest)!=1 and int(selec_rest) != 2):
            selec_rest = input('Error. Ingrese una opcion valida: ')
        
        if int(selec_rest) ==1:
            self.search_products()
        elif int(selec_rest)==2:
            self.buy_productos()

    
    def search_products(self):
        selec_product = input('Ingrese el producto que desea buscar: ').title()
        while selec_product.isnumeric():
            selec_product = input('Error. Ingrese el producto que desea buscar: ').title()
    
        found = False

        for estadio in self.estadios:
            for restaurant in estadio.restaurants:
                for producto in restaurant.products:
                    if producto.name == selec_product:
                        found = True
                        print(f'''
        {estadio.name}:
        {restaurant.name}

        {producto.mostrar()}
        ''')
    
        if not found:
            print(f"No se encontro el producto")
    

    def buy_productos(self):
        
        cedula_cliente = input("Ingrese su cedula: ")

        compra = False
        for client in self.clientes:
            if int(client.cedula) == int(cedula_cliente):
                current_client = client
                for ticket in client.tickets:
                    print(ticket.mostrar())
                ticket_id = input("Ingrese el ticket ID del partido en que se encuentra: ")
                if isinstance(ticket, VIP):
                        compra = True
    
                else:
                    print("El ticket adquirido no es VIP y en consecuencia no tiene acceso a los restaurantes!")
                    break

        if compra:
            for ticket in self.tickets:
                if ticket.ticket_id == int(ticket_id):
                    current_ticket = ticket
                    for restaurant in ticket.match.stadium.restaurants:
                        for i, products in enumerate(restaurant.products):
                            print(f"{i+1}. {products.mostrar()}")
                            current_products = restaurant.products

            selec_compra = input("Numero del producto: ")
            while not selec_compra.isnumeric() or int(selec_compra) > len(current_products) or int(selec_compra) < 1:
                op_compra = input("Error. Numero del producto: ")
            
            compra = current_products[int(selec_compra)-1]
            for product in current_products:
                if product == compra:
                    if product.tipo == "bebida":
                            if product.adicional == 'alcoholic':
                                if int(current_client.age) < 18:
                                    print("Usted no tiene la edad para comprar bebidas alcoholicas.")
                                    break
                    descuento = 0
                    if self.es_perfecto(int(current_client.cedula)):
                        descuento = compra.price * 0.15
                    current_factura = Factura(compra, descuento)
                    print(current_factura.mostrar())

                    confirmation = input(f"Desea comprar {product.name}?\n1. Si\n2. No\n")
                    while not confirmation.isnumeric() or int(confirmation) < 1 or int(confirmation) > 2:
                        confirmation = input(f"Error. Desea comprar {product.name}?\n1. Si\n2. No\n")
                    
                    if int(confirmation) == 1:
                        compra.stock = compra.stock - 1
                        lista_compras = current_ticket.compras
                        lista_compras.append(current_factura)
                        print("Su compra ha sido registrada!")
            
    #estadisticas
    def estadisticas(self):
        print('''
        1. Promedio gastos VIP
        2. Asistencia
        3. Boletos vendidos
        4. Clientes
        ''')

        selec_estadisticas = input("Ingrese una de las opciones:   ")
        while not selec_estadisticas.isnumeric() or int(selec_estadisticas) not in range (1,5):
            selec_estadisticas = input("Ingrese una de las opciones:   ")
        
        if int(selec_estadisticas) ==1:
            self.gastos_vip()
        elif int(selec_estadisticas) ==2:
            self.orden_asistencia()
        elif int(selec_estadisticas) ==3:
            self.ticket_vendidos()
        elif int(selec_estadisticas) ==4:
            self.mejor_cliente()
    
    def gastos_vip(self):

        tot_entradas_vip = 0
        tot_rest = 0
        cant_tickets_vip = 0
        for ticket in self.tickets:
            if isinstance(ticket, VIP):
                    cant_tickets_vip += 1
                    tot_entradas_vip += ticket.total
                    for compra in ticket.compras:
                        tot_rest += compra.total
                    total_vip = tot_entradas_vip + tot_rest

        print(f'''
        
        TOTAL DE VENTAS VIP: {total_vip}
        PROMEDIO: {total_vip/cant_tickets_vip}

        ''')
    
    def orden_asistencia(self):
        self.partidos.sort(key = lambda partido: len(partido.asistencia), reverse = True)
        for i, partido in enumerate(self.partidos):
            entradas_vendidas = len(partido.seats_vip) + len(partido.seats_gen)
            asistencias = len(partido.asistencia)
            print(f'''
        {i+1}. ---{partido.home.name} VS {partido.away.name}---

            Stadio :{partido.stadium.name}
            Entradas vendidas: {entradas_vendidas}
            Asistencia :{asistencias}
            Relacion : {asistencias}// {entradas_vendidas}
                ''')
    
    def ticket_vendidos(self):
        max_cant = 0
        for partido in self.partidos:
            vip = len(partido.seats_vip)
            general = len(partido.seats_gen)
            tot = vip + general
            if tot > max_cant:
                partido_max = partido
        
        print(f"El partido con mayor cantidad de tickets vendidos: {partido_max.mostrar()}")

    def mejor_cliente(self):
        self.clientes.sort(key= lambda cliente: len(cliente.tickets), reverse = True)

        for i, cliente in enumerate (self.clientes):
            if i < 3:
                print(f"{i+1}. {cliente.mostrar_atributos()}")


        



    

                
      






