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

# *Funciones principales
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
