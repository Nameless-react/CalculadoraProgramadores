from tabulate import tabulate
import re
from conversor import binario_decimal

# *Networks subnetting functions

def plusOctet(direccion1, direccion2):
    sobra = 0
    new_direction = []
    for octeto1, octeto2 in zip(direccion1[::-1], direccion2[::-1]):
        suma = int(octeto1) + int(octeto2) + sobra
        sobra = 0


        if suma > 255:
            sobra = suma - 255
            new_direction.append(str(sobra - 1))
            sobra = 1
            continue

        new_direction.append(str(suma))
    
    return new_direction[::-1]

def minusOctet(direccion1, direccion2):
    sobra = 0
    new_direction = []
    for octeto1, octeto2 in zip(direccion1[::-1], direccion2[::-1]):

        suma = int(octeto1) - int(octeto2) - sobra
        
        sobra = 0
        if suma < 0:
            sobra = abs(suma)
            new_direction.append("255")
            continue

        new_direction.append(str(suma))

    return new_direction[::-1]


def subneteoRed():
    column_names = ["Red", "IP", "Broadcast", "WildCard", "Máscara", "Máscara decimal", "Hosts totales", "Hosts requeridos", "Rango"]
    info_networks = []

    redes = 0
    try:
        redes = int(input("Ingrese la cantidad de redes que desea:\n"))
    except ValueError as e:
        print("Cantidad de redes invalida")
        return
    

    while True:
        direccion_red = input("Ingrese la direccion de red:\n")
        match = re.fullmatch("[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*", direccion_red)
        if match:
            break



    broadcast = []
    direccion_red = direccion_red.split(".")
    direcciones = [direccion_red]


    for i in range(redes): 
        mascara_subred_decimal = []
        full_mask = [255, 255, 255, 255]
        hosts_requeridos = int(input("Ingrese la cantidad de host que desea en orden descendiente:\n"))

        # *Determinación de la máscara de red
        host = 0
        while host < hosts_requeridos:
            if 2**host - 2 >= hosts_requeridos:
                break 
            host += 1

        mascara_subred = 32 - host
        
        
        # *Máscara de subred en notación decimal
        for j in range(4):
            if mascara_subred >= 8:
                mascara_subred_decimal.append(str(binario_decimal("11111111")))
                mascara_subred -= 8
                continue

            mascara_subred_decimal.append(str(binario_decimal(("1" * mascara_subred).zfill(8)[::-1])))
            mascara_subred = 0
        # *Cálculo de la wildCard de la subred
        wild_card = [str(full - int(octeto)) for full, octeto in zip(full_mask, mascara_subred_decimal)]
    
    
        # *BroadCast y direcciones de las subredes
        if i == 0:
            broadcast.append(plusOctet(wild_card, direccion_red))
        else:
            direcciones.append(plusOctet(broadcast[len(broadcast) - 1], ["0", "0", "0", "1"]))
            broadcast.append(plusOctet(wild_card, direcciones[i]))
        


        # *Guardar información de cada subred
        info_networks.append([f"Red {i + 1}",
                        '.'.join(map(lambda x: str(x), direcciones[i])),
                        '.'.join(map(lambda x: str(x), broadcast[i])),
                        '.'.join(wild_card),
                        32 - host, 
                        '.'.join(mascara_subred_decimal),
                        2**host,
                        hosts_requeridos,
                        '.'.join(map(lambda x: str(x), plusOctet(direcciones[i], ["0", "0", "0", "1"]))) + " - " + '.'.join(map(lambda x: str(x), minusOctet(broadcast[i], ["0", "0", "0", "1"]))),
                        ])
    print(tabulate(info_networks, headers=column_names, tablefmt="fancy_grid"))