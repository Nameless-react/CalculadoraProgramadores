#!/usr/bin/env python3
from subneteo import subneteoRed
from conversor import functions


def conversiones():
    while True:
        operacion = input("""Digite el tipo de número: 
b) binario
d) decimal
h) hexadecimal
s) salir
""").lower()
        if operacion == "s":
            break
        action = functions.get(operacion, lambda x: print(f"\33[31m\nOperación '{operacion}' no valida\n\033[0m"))
        if not action("0"):
            continue

        numero = input("Ingrese un numero a convertir:\n").upper()
        print(f"\n{'#' * 20}\n{action(numero)}\n{'#' * 20}\n")


def main():
    while True:
        option = input(f"""{'#' * 20} ¿Que Desea realizar? {'#' * 20}
c) conversiones
n) subneteo de red (IPv4)
s) salir
""").lower()
        
        if option == "c":
            conversiones()
        elif option == "n":
            subneteoRed()
        elif option == "s":
            break

if __name__ == "__main__":
    main()
