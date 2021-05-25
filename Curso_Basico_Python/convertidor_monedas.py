
import http.client
import json


def api_call(id_currency):

    conn = http.client.HTTPSConnection(
        "api.coingecko.com", timeout=10)  # (host:str, port:Optional [int], ...)

    url = f'/api/v3/simple/price?ids={id_currency}&vs_currencies=mxn'

    try:
        conn.request("GET", url)  # (method:str ,url:str, headers, ...)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
        price = data[id_currency]['mxn']

        return price
    except:
        return None


if __name__ == "__main__":
    print("""
        Convertidor de $ MXN a Criptomonedas
        
        1. Convertir de pesos a cardano (ada)
        2. Convertir de pesos a bitcoin (btc) 
        3. Convertir de pesos a ethereum (eth)
    """)

    option = int(input("Ingrese el numero de la opcion deseada: "))

    while (option < 1 or option > 3):
        print("\nOpcion no disponible, intentelo de nuevo! ")
        option = int(input("\nIngrese el numero de la opcion deseada: "))

    amount = float(input("Ingrese la cantidad en $ MXN: "))

    currency = ""
    symbol = ""

    if option == 1:
        currency = "cardano"
        price = api_call(currency)
        symbol = "ada"
    elif option == 2:
        currency = "bitcoin"
        price = api_call(currency)
        symbol = "btc"
    else:
        currency = "ethereum"
        price = api_call(currency)
        symbol = "eth"

    if price:
        exchange = amount/price
        exchange = round(exchange, 5)
        print(f"""-----------------------resultado---------------------------

        pesos (mxn): {amount} = {exchange} {currency}({symbol})

----------------------------------------------------------------------
        """)
    else:
        print("Lo sentimos, hubo un error en la conversion. Intente de nuevo")
admin