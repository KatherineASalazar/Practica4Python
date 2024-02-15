
# Implemente un programa donde se le solicitará al usuario la ruta de un archivo .py (nombre y
# ruta). Y retorne la cantidad de líneas de código de ese archivo, excluyendo los comentarios y
# líneas en blanco. Si el usuario ingresa una ruta inválida o si el nombre del archivo no termina en
# .py, su programa no retornará ningún resultado.

def contar_lineas_codigo(archivo):
    try:
        if not archivo.endswith('.py'):
            print("El archivo no es un archivo Python (.py).")
            return

        with open(archivo, 'r') as f:
            lineas_codigo = 0
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    lineas_codigo += 1

        print(f"El número de líneas de código en {archivo} es: {lineas_codigo}")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")

if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)
    