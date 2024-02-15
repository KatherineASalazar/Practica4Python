# Empleando la base de datos del problema anterior. Cree una tabla llamada ‘bitcoin‘ la cual contenga
# información del precio del bitcoin del día.
# La información para guardar en la tabla será en moneda USD, GBP, EUR, PEN. Deberá tomar como base
# lo realizado en el problema1. Para calcular el precio en PEN deberá considerar el tipo de cambio de
# SUNAT al día de realizada la consulta al api Bitcoin.
# Asegúrese de crear las columnas necesarias para este ejercicio, además de añadir una columna de fecha
# que almacenará los datos en que se tomaron los datos.
# Finalmente deberá consultar la base de datos para calcular el precio de comprar de 10 bitcoins en
# moneda PEN y EUR

import requests
import sqlite3
import datetime

def obtener_tipo_cambio_soles():
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT precio_compra FROM sunat_info ORDER BY fecha DESC LIMIT 1")
    precio_compra_soles = cursor.fetchone()[0]
    conexion.close()
    return precio_compra_soles

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice/PEN.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        precio_btc_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        precio_btc_gbp = float(data['bpi']['GBP']['rate'].replace(',', ''))
        precio_btc_eur = float(data['bpi']['EUR']['rate'].replace(',', ''))
        precio_btc_pen = float(data['bpi']['PEN']['rate'].replace(',', ''))

        precio_compra_soles = obtener_tipo_cambio_soles()
        precio_btc_pen = precio_btc_usd * precio_compra_soles

        return precio_btc_usd, precio_btc_gbp, precio_btc_eur, precio_btc_pen
    else:
        print("Error al obtener los datos del precio de Bitcoin.")
        return None

def guardar_datos_bitcoin():
    precios = obtener_precio_bitcoin()
    if precios:
        fecha = datetime.date.today()
        conexion = sqlite3.connect('base.db')
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                            fecha TEXT PRIMARY KEY,
                            precio_usd REAL,
                            precio_gbp REAL,
                            precio_eur REAL,
                            precio_pen REAL
                        )''')
        cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) 
                          VALUES (?, ?, ?, ?, ?)''', (fecha, *precios))
        conexion.commit()
        conexion.close()
        print("Datos de Bitcoin guardados correctamente.")
    else:
        print("No se pudieron obtener los datos de Bitcoin.")

def precio_compra_10_bitcoins():
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    precios = cursor.fetchone()
    conexion.close()

    if precios:
        precio_pen = precios[0]
        precio_eur = precios[1]
        precio_total_pen = precio_pen * 10
        precio_total_eur = precio_eur * 10
        print(f"Precio de comprar 10 bitcoins en PEN: {precio_total_pen} PEN")
        print(f"Precio de comprar 10 bitcoins en EUR: {precio_total_eur} EUR")
    else:
        print("No se encontraron datos de Bitcoin en la base de datos.")

if __name__ == "__main__":
    guardar_datos_bitcoin()
    precio_compra_10_bitcoins()
