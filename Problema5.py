# Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones,
# también puede usar un menú para organizar su programa):
#- Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre
#  tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
#- Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
#  multiplicar de ese número, donde “n” es el número introducido, y la muestre por pantalla. 
#  Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
#- Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese
# número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje
#  por pantalla informando de ello.


import os

def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return
    
    with open(f"tabla-{numero}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{numero} x {i} = {numero*i}\n")
    print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            print(f"Tabla de multiplicar del {numero}:")
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe. Guardar tabla-{numero}.txt primero")

def mostrar_linea_tabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lines = file.readlines()
            if 1 <= linea <= len(lines):
                print(f"Línea {linea}: {lines[linea-1].strip()}")
            else:
                print("El número de línea está fuera de rango.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe. Guardar tabla-{numero}.txt primero")

def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea ver: "))
            mostrar_linea_tabla(numero, linea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")