#Almacene los datos de precio de Bitcoin en un archivo txt con un formato que consideré
#apropiado.

import requests
from datetime import datetime

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return float(data["bpi"]["USD"]["rate"].replace(",", ""))
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def save_price_to_file(price):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("bitcoin_prices.txt", "a") as file:
        file.write(f"{timestamp}: ${price:.2f} USD\n")

def main():
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        save_price_to_file(bitcoin_price)
        print("Datos de precio de Bitcoin guardados exitosamente en bitcoin_prices.txt")

if __name__ == "__main__":
    main()