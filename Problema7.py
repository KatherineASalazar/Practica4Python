# Emplee el API de SUNAT que corresponda para obtener el precio de compra y
# venta del dólar durante todo el 2023. Almacene dicha información en base de datos ‘base.db’ con
# nombre de tabla sunat_info.
# Finalmente deberá mostrar el contenido de dicha tabla.
# Lee la documentación del API: https://apis.net.pe/api-tipo-cambio.html


import requests
import sqlite3

def obtener_tipo_cambio_anual():
    # URL base de la API de SUNAT
    url_base = "https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha"
    
    # Creamos una conexión a la base de datos SQLite
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()

    # Creamos la tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        precio_compra REAL,
                        precio_venta REAL
                    )''')

    # Iteramos sobre cada día del año 2023
    for i in range(1, 13):  # Meses
        for j in range(1, 32):  # Días
            fecha = f"2023-{i:02d}-{j:02d}"

            # Hacemos la solicitud a la API para obtener el tipo de cambio de ese día
            response = requests.get(f"{url_base}={fecha}")

            if response.status_code == 200:
                tipo_cambio = response.json()['tipo_cambio']
                precio_compra = tipo_cambio['compra']
                precio_venta = tipo_cambio['venta']
                # Insertamos los datos en la base de datos
                cursor.execute('''INSERT OR IGNORE INTO sunat_info (fecha, precio_compra, precio_venta) 
                                  VALUES (?, ?, ?)''', (fecha, precio_compra, precio_venta))
                print(f"Datos para {fecha} insertados en la base de datos.")
            else:
                print(f"No se pudo obtener datos para {fecha}")

    # Guardamos los cambios y cerramos la conexión
    conexion.commit()
    conexion.close()

def mostrar_contenido_tabla():
    # Conectamos a la base de datos y mostramos el contenido de la tabla
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    conexion.close()

if __name__ == "__main__":
    obtener_tipo_cambio_anual()
    print("\nContenido de la tabla 'sunat_info':")
    mostrar_contenido_tabla()




