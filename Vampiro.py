from itertools import permutations
def es_vampiro(client, ticket_selected):
    '''calcula si la cedula de un cliente es un numero vampiro y regresa el descuento correspondiente'''
    number = client.cedula
    vampiro = False
    if len(str(number))==7:
        return 0 
    else:
        p = permutations(str(number)), len(str(number))
        p_list = list(p)
        for n in p_list:
            joined = ''.join(n)
            x,y = joined[:int(len(joined)/2)], joined[int(len(joined)/2):]
            if x[-1]==0 and y[-1]==0:
                continue
            if int(x)*int(y)==int(number):
                vampiro = True
    if vampiro == False:
        return 0
    else:
        discount = ticket_selected.price*0.5
        return discount