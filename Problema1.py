#En este problema debe generar un programa que realice:
#- Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad
#de bitcoins que posee el usuario.
#- Consulte la API del índice de precios de Bitcoin de CoinDesk en el siguiente link
#(https://api.coindesk.com/v1/bpi/currentprice.json), la cual retornará un objeto JSON,
#entre cuyas claves anidadas encontrará el precio actual de Bitcoin como un número
#decimal. Asegúrese de detectar cualquier excepción, como el siguiente código:

#import requests
#try:
#...
#except requests.RequestException:
#...
#- Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando , como
#separador de miles.

pip install requests

import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return float(data["bpi"]["USD"]["rate"].replace(",", ""))
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        while True:
            try:
                n_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
                if n_bitcoins < 0:
                    print("Por favor, ingrese un número positivo.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número válido.")

        total_cost_usd = n_bitcoins * bitcoin_price
        print(f"El costo actual de {n_bitcoins:,.4f} bitcoins es: ${total_cost_usd:,.4f} USD")

if __name__ == "__main__":
    main()