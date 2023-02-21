from tabulate import tabulate
import re

hexa = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
}

def binario(numero):
    decimal = binarioDecimal(str(numero))
    hexadecimal = binarioHexadecimal(str(numero))
    return f"Binario: {str(numero).zfill(4)}\nDecimal: {decimal}\nHexadecimal: {hexadecimal}"


def decimal(numero):
    binario = decimalBinario(numero)
    hexadecimal = decimalHexadecimal(numero)
    return f"Decimal: {numero}\nBinario: {binario.zfill(4)}\nHexadecimal: {hexadecimal}"

def hexadecimal(numero):
    for i in numero:
        if i not in hexa:
            return "\33[31m\nNúmero hexadecimal no valido\n\033[0m"


    binario = hexadecimalBinario(numero)
    decimal = hexadecimalDecimal(numero)
    return f"Hexadecimal: {numero}\nBinario: {binario.zfill(4)}\nDecimal: {decimal}"






def binarioDecimal(numero):
    binario = numero[::-1]
    decimal = 0
    for index, number in enumerate(binario):
        exponencial = 2**int(index)
        if int(number) == 1:
            decimal += exponencial

    return decimal


def decimalBinario(numero):
    decimal = int(numero)
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        decimal //= 2
        binario += str(residuo)

    return binario[::-1]

def hexadecimalDecimal(numero):
    hexadecimal = numero.upper()
    return int(hexadecimal, 16)

def binarioHexadecimal(binario):
    return hex(int(binario, 2))[2:].upper()

def decimalHexadecimal(numero):
    decimal = int(numero)
    return hex(decimal)[2:].upper()

def hexadecimalBinario(numero):
    hexadecimal = numero.upper()
    return bin(int(hexadecimal, 16))[2:]

functions = {
    "b": binario,
    "d": decimal,
    "h": hexadecimal,
}



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