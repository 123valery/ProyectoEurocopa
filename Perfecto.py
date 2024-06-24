def es_perfecto(client, sub_total):
    '''calcula si el subtotal de una compra es un numero perfecto y regresa el descuento correspondiente '''
    number =client.cedula
    divisores = []
    for n in range(1, number):
        if number%n ==0:
            divisores.append(n)
    sum_divisores = sum(divisores)
    if sum_divisores == number:
        discount = sub_total *0.15
        return discount
    else:
        return 0
