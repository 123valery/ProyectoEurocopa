import requests
from Equipo import Equipo
from Partido import Partido
from Estadio import Estadio
from Restaurant import Restaurant
from Bebida import Bebida
from Alimento import Alimento
from Cliente import Cliente
from General import General
from VIP import VIP
from Vampiro import es_vampiro
from Perfecto import es_perfecto

def api_manager():
    '''descarga la informacion del programa de la API en GitHub'''

    url_equipos = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'
    r_equipos = requests.get(url_equipos)
    info_equipos = r_equipos.json()

    url_partidos = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'
    r_partidos = requests.get(url_partidos)
    info_partidos = r_partidos.json()

    url_estadios = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
    r_estadios = requests.get(url_estadios)
    info_estadios = r_estadios.json()

    return info_equipos, info_partidos, info_estadios


def manage_equipos(info_equipos):
    '''tranforma la información de la API sobre equipos en objetos Equipo'''
    equipos = []
    for equipo in info_equipos:
        equipo = Equipo(equipo['id'],equipo['code'], equipo['name'], equipo['group'])
        equipos.append(equipo)
    return equipos

def manage_partidos(info_partidos):
    '''tranforma la información de la API sobre partidos en objetos Partido'''
    partidos = []
    for partido in info_partidos:

        partido = Partido(partido['home'],partido['away'], partido['date'], partido['stadium_id'], partido['id'], 0,0)
        partidos.append(partido)
    return partidos

def manage_estadios(info_estadios):
    '''tranforma la información de la API sobre estadios en objetos Estadio'''
    estadios = []
    for estadio in info_estadios:

        estadio = Estadio(estadio['id'],estadio['name'], estadio['city'], estadio['capacity'],estadio['restaurants'])
        estadios.append(estadio)
    return estadios

def manage_restaurantes(estadios):
    '''transforma la informacion de los restaurantes en los estadios a objetos Restaurante y Alimento/Bebida '''
    restaurantes = []
    for estadio in estadios:
        restaurantes_estadio = []
        for restaurante in estadio.restaurants:
            restaurante = Restaurant(restaurante['name'], restaurante['products'])
            restaurant_products = []
            for product in restaurante.products:
                if product['adicional'] == 'alcoholic' or product['adicional']== 'non-alcoholic':
                    new_product = Bebida(product['name'], product['price'], product['quantity'], product['adicional'])
                    restaurant_products.append(new_product)
                else:
                    new_product = Alimento(product['name'], product['price'], product['quantity'], product['adicional'])
                    restaurant_products.append(new_product)

            restaurante.products = restaurant_products
            restaurantes.append(restaurante)
        estadio.restaurants = restaurantes_estadio
    return estadios, restaurantes

def manage_objects_partidos(partidos,equipos,estadios):
    '''transforma la informacion de partidos pertinente a objetos dentro del objeto Partido'''
    for partido in partidos:
        for equipo in equipos:
            if equipo.name==partido.home_team:
                partido.home_team=equipo

    for partido in partidos:
        for equipo in equipos:
            if equipo.name==partido.away_team:
                partido.away_team=equipo

    for partido in partidos:
        for estadio in estadios:
            if estadio.id==partido.stadium_id:
                partido.stadium_id=estadio

    return partidos

def add_iva_products(estadios,restaurantes):
    '''agrega el %16 de IVA a los productos del restaurante'''
    for estadio in estadios:
        for restaurant in estadio.restaurants:
            for product in restaurant.products:
                iva=product.price*0.16
                product.total=iva+product.price

    for restaurant in restaurantes:
        for product in restaurant.products:
            iva=product.price*0.16
            product.total=iva+product.price

    return estadios,restaurantes


def get_option():
    '''recibe y valida la opcion de menu que desea escoger el usuario'''
    while True:
        try:
            option=int(input('Para continuar seleccione una accion a realizar:\n1 - Comprar entradas\n2 - Gestion de partidos\n3 - Buscar partidos\n4 - Ingresar en Restaurante\n5 - Buscar productos en Restaurantes\n6 - Mostrar Estadisticas\n7 - Salir y Guardar\n=> '))
            if option!=1 and option!=2 and option!=3 and option!=4 and option!=5 and option!=6 and option!=7:
                raise Exception
            else:
                break
                
        except:
            print('\ningreso invalido!')
    
    return option

def register_client(clients):
    '''registra la informacion de un nuevo cliente y la guarda en el programa como objeto Cliente'''
    print('\nAntes de continuar con la compra, debe registrarse en la base de datos')

    name = input('Ingrese su nombre:  ')
    while not name.isalpha():
        name = input('\n Nombre invalido\nIngrese su nombre:  ')
    
    while True:
        try:
            cedula = int(input('Ingrese su numero de cedula:  '))
            if len(str(cedula))>8:
                print('/n la cedula ingresada tiene mas de 8 digitos')
            if len (str(cedula)<7):
                print('/n la cedula ingresada tiene menos de 7 digitos')
                raise Exception
            if len(clients) != 0:
                for client in clients:
                    if cedula == client.cedula:
                        print('la cedula ya se encuentra en la base de datos\n')
                        raise Exception
            break
        except:
            print('\nIngreso invalido, intente de nuevo\n')
    
    while True:
        try:
            age = int(input('Ingrese su edad:  '))
            if age<9 or age>100:
                raise Exception
            else:
                break
        
        except:
            print('\nEsta seguro que esta es su edad? Intente de nuevo\n')
        tickets = []
        new_client = Cliente(name, cedula, age, tickets)
        clients.append(new_client)

        #Agregar lo de txt
    return clients, new_client

def find_client(clients):
    '''busca al cliente en la base de datos del programa'''
    while True:
        try:
            cedula = int(input('Ingrese su numero de cedula para ubicar sus datos en el sistema:  '))
            if len(str(cedula))>8:
                raise Exception
            if len(str(cedula))<7:
                raise Exception
            break
        except:
            print('\nIngreso invalido, intente de nuevo\n')
        
        found = False
        for cliente in clients:
            if cedula == cliente.cedula:
                found = True
                print('\nbienvenido', cliente.name, '!')
                cliente_actual  = cliente
                break
        if found == False:
            print('\nNo se ha encontrado la cedula en la base de datos !')
            clients, cliente_actual = register_client(clients)

    return clients, cliente_actual

def select_match(partidos):
    '''funcion que permite al cliente seleccionar un partido para comprar entradas '''
    found = False
    while True:
        try:
            match_selected = input('indique el "id" que corresponde al partido que desea ver:  ')
            for partido in partidos:
                if match_selected == partido.id:
                    found = True
                    match_selected = partido
                    if found:
                        break
            if found == False:
                raise Exception
            break
        except:
            print('\nel id no fue encontrado\n')
    print('\n   PARTIDO SELECCIONADO')
    match_selected.show()
    return match_selected

def ticket_selection(match_selected, tickets_vendidos):
    '''funcion que permite al cliente elegir el tipo de ticket, regresa un objeto General/VIP'''
    vip_sold = []
    general_sold = []
    for ticket in tickets_vendidos:
        if ticket.match ==match_selected:
            if ticket.price == 35:
                general_sold.append(ticket.seat)
            else:
                vip_sold.append(ticket.seat)
    capacity_stadium = match_selected.stadium_id.capacity
    general = capacity_stadium[0]
    vip = capacity_stadium[1]
    if len(general_sold)>= int(general):
        type = input('\nPara el partido seleccionado quedan dispobibles entradas tipo:\n2 - VIP\n   precio: 75$\n   incluye:acceso al restaurante del estadio\n=> ')
        while not type.isnumeric() or int(type) != 2:
            type = input('\n seleccion invalida\n Para el partido seleccionado quedan dispobibles entradas tipo:\n2 - VIP\n   precio: 75$\n   incluye:acceso al restaurante del estadio\n=> ')
        
    elif len(vip_sold)>= int(vip):
        type = input('\nPara el partido seleccionado quedan dispobibles entradas tipo:\n1 - General\n   precio: 35$\n   incluye: vista del partido desde su asiento\n=> ')
        while not type.isnumeric() or int(type) != 1:
            type = input('\nIngreso invalido\n Para el partido seleccionado quedan dispobibles entradas tipo:\n1 - General\n   precio: 35$\n   incluye: vista del partido desde su asiento\n=> ')
    
    else:
        type = input('\nPuede escoger entre dos tipos de entrada:\n1-GENERAL\n  precio: 35$\n  inclue: vista del partido desde su asiento desde su asiento\n2-VIP\n  precio: 75\n  incluye:acceso al restaurante del estadio\n=> ')
        while not type.isnumeric() or int(type) != 1 or int(type) != 2:
            type = input('\nIngreso invalido\nPuede escoger entre dos tipos de entrada:\n1-GENERAL\n  precio: 35$\n  inclue: vista del partido desde su asiento desde su asiento\n2-VIP\n  precio: 75\n  incluye:acceso al restaurante del estadio\n=> ')
    
    if int(type)== 1:
        ticket_selected=General(None, len(tickets_vendidos), match_selected, False)
    else:
        ticket_selected=VIP(None, len(tickets_vendidos), match_selected, False)

    return ticket_selected

def seat_selection(ticket_selected, partido, tickets_vendidos):
    '''imprime el mapa del estadio y valida la eleccion del asiento'''
    taken_seats = []
    for ticket in tickets_vendidos:
        if ticket.match == partido:
            taken_seats.append(ticket.seat)
    
    capacity_stadium = partido.stadium_id.capacity
    general = capacity_stadium[0]
    vip = capacity_stadium[1]
    seat_amount = general + vip
    column_count = 'A'
    for a in range (int(seat_amount/10)):
        fila = ['XX' if str(column_count)+ str(b+1)in taken_seats else str(column_count) +str(b+1) for b in range(-1,9)]
        column_count = chr(ord(column_count)+1)
        print(''.join(fila))
    print('\n   CAMPO DE JUEGO    ')
    print(' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    print('|              |              |')
    print('| _           _| _          _ |')
    print('|  |         |    |        |  |')
    print('| _|         | _ _|        |_ |')
    print('|              |              |')
    print('| _ _ _ _ _ _ _|_ _ _ _ _ _ _ |')
    
    while True:
        try:
            seat_selected = input('\nXX - Ocupado\nSeleccione el asiento de su preferencia segun el mapa:  ').upper()
            if len(seat_selected) != 2:
                print('\nrecuerde ingresar su asiento en formato "A0"  ')
                raise Exception
            if not seat_selected[0].isalpha():
                raise Exception
            for seat in taken_seats:
                if seat_selected == seat:
                    print('\nEste asiento ya fue vendido')
                    raise Exception
            in_range= False
            for leter in range(ord(column_count)+1):
                if leter == ord(seat_selected[0]):
                    in_range = True
                    break
            if in_range == False:
                print('\La fila seleccionada no existe en el estadio')
                raise Exception
            valid = False
            for column in range(0,10):
                if column == int(seat_selected[1]):
                    valid = True
                    break
            if valid == False:
                print('\nEl numero de asiento seleccionado no existe en el estadio')
                raise Exception
            break
        except:
            print('intente de nuevo!')

    ticket_selected.seat = seat_selected
    ticket_selected.match = partido
    return ticket_selected


def ticket_total(ticket_selected,client):
    '''muestra el resumen de compra del cliente, incluye descuentos'''
    ticket_selected.discount=es_vampiro(client,ticket_selected)
    subtotal=ticket_selected.price-ticket_selected.discount
    ticket_selected.iva=subtotal*0.16
    ticket_selected.total=subtotal+ticket_selected.iva
    print('\n',client.name,'este es el resumen de su compra:\n')
    print('     subtotal: $',subtotal)
    print('     descuentos: $',ticket_selected.discount)
    print('     IVA: $',ticket_selected.iva)
    print('     total: $',ticket_selected.total)
    return ticket_selected

def buy_ticket(client,ticket_selected, codigos_tickets, tickets_vendidos, match_selected):
    '''pregunta al cliente si quiere o no continuar con la compra, si continua se modifica los datos del programa'''
    while True:
        try:
            proceed = int(input('\nDesea finalizar la compra?\n1-Si\n2-No\n=> '))
            if proceed != 1 and proceed != 2:
                raise Exception
            else:
                break
        except:
            print('\nopcion invalida\n')
    
    if proceed ==1:
        match_selected.tickets_sold +=1
        client.tickets.append(ticket_selected)
        codigos_tickets.append(ticket_selected.code)
        tickets_vendidos.append(ticket_selected)
        print('\nEl pago se ha completado exitosamente!\n')
        return client, codigos_tickets, tickets_vendidos, match_selected
    else:
        print('\nLa compra ha sido cancelada!\n')
        return client, codigos_tickets, tickets_vendidos, match_selected
    
def ticket_manager(codigos_usados, codigos_tickets, tickets_vendidos):
    '''modulo administrativo de entradas, se ingrresa un codigo de entrada y se valida si el numero esta en la base de datos, de ser asi se marca el ticket como usado'''
    while True:
        try:
            code = int(input('\nIngrese el numero que corresponde al codigo unico del ticket que va a ser usado: '))
            break
        except:
            print('\nIngreso invalido, intente de nuevo')
    for codigo in codigos_usados:
        if codigo == code:
            print('\nel codigo ya fue utilizado, el ingreso es unico')
            return codigos_usados, codigos_tickets, tickets_vendidos
    found = False
    for codigo in codigos_tickets:
        if codigo == code:
            found = True
            break

    if found:
        print('\nse ha encontrado el codigo unico en la base de datos\nel ticket se utilizo con exito!')
        for ticket in tickets_vendidos:
            if ticket.code == code:
                ticket.used = True
                return codigos_usados, codigos_tickets, tickets_vendidos
            else:
                print('\nel codigo ingresado no existe en la base de datos\nel ticket no puede ser validado para su uso')
                return codigos_usados, codigos_tickets, tickets_vendidos

def search_by_country(equipos, partidos):
    '''funcion de busqueda de partidos por pais'''
    print('---PAISES---')
    for equipo in equipos:
        print(equipo.name)
    while True:
        try:
            country = input('Indique el pais para mostrar los partidos del equipo:  ').lower()
            found = False
            for equipo in equipos:
                if country==equipo.name.lower():
                    found = True
                    break
            if found == False:
                raise Exception
            else:
                break
        except:
            print('\nIngreso invalido! intente de nuevo\n')
    
    for partido in partidos:
        if partido.home_team.lower() == country:
            partido.show()
        if partido.away_team.lower() == country:
            partido.show()

def search_by_stadium(estadios, partidos):
    '''funcion de busqueda de partidos segun estadio'''
    print('---ESTADIOS---')
    for estadio in estadios:
        print(estadio.id, '-', estadio.name)
    
    while True:
        try:
            stadium = int(input('Indique el id del estadio para mostrar los partidos del recinto:  '))
            found = False
            for estadio in estadios:
                if stadium==estadio.id:
                    found = True
                    break
            if found == False:
                raise Exception
            else:
                break
        except:
            print('\ningreso invalido! intente de nuevo\n')
    
    for partido in partidos:
        if partido.stadium_id.id == stadium:
            partido.show()

def search_by_date(partidos):
    '''funcion de busqueda de partidos segun fecha'''
    while True:
        try:
            date = input('Ingrese un dia entre 06/14 y 06/26')
            if len(date) != 4 and len(date) !=5:
                raise Exception
            if int(date[0]) !=0 and int(date[1]) !=6:
                raise Exception
            if date[2] != '/':
                print('\nrecuerde separar el mes y el dia con "/"')
                raise Exception
            
            if int(date[1])==6:
                if int((date[3]) + (date[4])) < 14 and int((date[3])+(date[4]))>30:
                    raise Exception
            break
        
        except:
            print('\ningreso invalido! intente de nuevo\n')
    
    for partido in partidos:
        if len(date)==5:
            if date == (partido.date[0] + partido.date[1]+ partido.date[2]+partido.date[3]+partido.date[4]):
                partido.show()

def get_cedula():
    '''valida el ingreso de la cedula del cliente'''
    while True:
        try:
            cedula = int(input('\nPor favor ingrese su numero de cedula para verificar que adquirio una entrada VIP: '))
            if len(str(cedula))>8:
                raise Exception
            if len(str(cedula))<7:
                raise Exception
            break
        except:
            print('\ningreso invalido, intente de nuevo\n')
    return cedula

def restaurant_manager(restaurant, client,ticket):
    '''modulo de manejo del restaurante y compra de productos'''
    print(f'\n---USTED SE ENCUENTRA EN {restaurant.name}---\n')
    print('     MENU')
    for product in restaurant.prodcuts:
        if client.age<18:
            if product.adicional!='alcoholic':
                product.show()
        else:
            product.show()
    cart = []
    print('\n*NOTA: el IVA de cada producto se inclute en el total del checkout')
    while True:
        try:
            selected_product_name = str(input('\nNombre del prodcuto que desea agrregar a la compra:  ')).lower()
            found = False
            for product in restaurant.products:
                if product.name.lower() == selected_product_name:
                    found = True
                    break
            if found == False:
                print('\nel producto no fue encontrado')
                raise Exception
            else:
                break
        except:
            print('\ningreso equivocado')
    for product in restaurant.products:
        if selected_product_name.lower() ==product.name.lower():
            selected_product = product
            cart.append(selected_product)
    while True:
        add = input('\n1-Agregar otro producto\n2-Checkout\n=> ')
        while not add.isnumeric() or int(add) != 1 or int(add) != 2:
            add = input('\nIngrese una opcion valida\n1-Agregar otro producto\n2-Checkout\n=> ')
        
        if int(add) ==1:
            while True:
                try:
                    selected_product_name = str(input('Nombre del producto que desea agregar a la compra  ')).lower()
                    found = False
                    for product in restaurant.products:
                        if product.name.lower() == selected_product_name.lower():
                            found = True
                            break
                    if found == False:
                        raise Exception
                    else:
                        break
                except:
                    print('\ningreso equivocado')

            for product in restaurant.products:
                if selected_product_name.lower() == product.name.lower():
                    selected_product = product
                    cart.append(selected_product)
        else:
            break
    
    sub_total= 0
    for item in cart:
        sub_total +=item.total
    discount = es_perfecto(client, sub_total)
    total = sub_total - discount
    total_f='{:.2f}'.format(total)
    print('\n--- CHECKOUT ---')
    print('cliente:',client.name)
    print('cedula:',client.cedula)
    print('-PRODUCTOS-')
    for item in cart:
        print(item.name)
    print('descuentos: $',discount)
    print(f'TOTAL: ${total_f}')

while True:
    




    

                
      






