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

j = api_manager()
print(j["capacity"]) 

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

