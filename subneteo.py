from tabulate import tabulate
import re
from conversor import binarioDecimal

# *Networks subnetting functions

def plusOctet(direccion1, direccion2):
    sobra = 0
    newDirection = []
    for octeto1, octeto2 in zip(direccion1[::-1], direccion2[::-1]):
        suma = int(octeto1) + int(octeto2) + sobra
        sobra = 0


        if suma > 255:
            sobra = suma - 255
            newDirection.append(str(sobra - 1))
            sobra = 1
            continue

        newDirection.append(str(suma))
    print(newDirection)
    return newDirection[::-1]

def minusOctet(direccion1, direccion2):
    sobra = 0
    newDirection = []
    for octeto1, octeto2 in zip(direccion1[::-1], direccion2[::-1]):

        suma = int(octeto1) - int(octeto2) - sobra
        print(suma)
        sobra = 0
        if suma < 0:
            sobra = abs(suma)
            newDirection.append("255")
            continue

        newDirection.append(str(suma))
    print(newDirection)
    return newDirection[::-1]


def subneteoRed():
    columnNames = ["Red", "IP", "Broadcast", "WildCard", "Máscara", "Máscara decimal", "Hosts totales", "Hosts requeridos", "Rango"]
    infoNetworks = []

    redes = 0
    try:
        redes = int(input("Ingrese la cantidad de redes que desea:\n"))
    except ValueError as e:
        print("Cantidad de redes invalida")
        return
    

    while True:
        direccionRed = input("Ingrese la direccion de red:\n")
        match = re.fullmatch("[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*", direccionRed)
        if match:
            break


    direccionRed = direccionRed.split(".")
    broadcast = []
    direcciones = [direccionRed]


    for i in range(redes): 
        mascaraSubredDecimal = []
        fullMask = [255, 255, 255, 255]
        hostsRequeridos = int(input("Ingrese la cantidad de host que desea en orden descendiente:\n"))

        # *Determinación de la máscara de red
        host = 0
        while host < hostsRequeridos:
            if 2**host - 2 >= hostsRequeridos:
                break 
            host += 1

        mascaraSubRed = 32 - host
        
        
        # *Máscara de subred en notación decimal
        for j in range(4):
            if mascaraSubRed >= 8:
                mascaraSubredDecimal.append(str(binarioDecimal("11111111")))
                mascaraSubRed -= 8
                continue

            mascaraSubredDecimal.append(str(binarioDecimal(("1" * mascaraSubRed).zfill(8)[::-1])))
            mascaraSubRed = 0
    
        wildCard = [str(full - int(octeto)) for full, octeto in zip(fullMask, mascaraSubredDecimal)]
    
    
        # *BroadCast y direcciones de las subredes
        if i == 0:
            broadcast.append(plusOctet(wildCard, direccionRed))
        else:
            direcciones.append(plusOctet(broadcast[len(broadcast) - 1], ["0", "0", "0", "1"]))
            broadcast.append(plusOctet(wildCard, direcciones[i]))
        


        # *Guardar información de cada subred
        infoNetworks.append([f"Red {i + 1}",
                        '.'.join(map(lambda x: str(x), direcciones[i])),
                        '.'.join(map(lambda x: str(x), broadcast[i])),
                        '.'.join(wildCard),
                        32 - host, 
                        '.'.join(mascaraSubredDecimal),
                        2**host,
                        hostsRequeridos,
                        '.'.join(map(lambda x: str(x), plusOctet(direcciones[i], ["0", "0", "0", "1"]))) + " - " + '.'.join(map(lambda x: str(x), minusOctet(broadcast[i], ["0", "0", "0", "1"]))),
                        ])
    print(tabulate(infoNetworks, headers=columnNames, tablefmt="fancy_grid"))