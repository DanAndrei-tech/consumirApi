import requests
from config import *
from models import *

allcoin = AllCoinApiIO()

#consulta de todas las monedas
allcoin.getAllCoins(APIKEY)

print (f"La cantidad de criptos son: {len(allcoin.lista_criptos)},\
       y la cantidad de no criptos son: {len(allcoin.lista_no_criptos)}")


moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:
    if moneda_cripto in allcoin.lista_criptos: 
      exchange = Exchange(moneda_cripto)

      try:
         exchange.updateExchange(APIKEY)
         print("{:,.2f}€".format(exchange.rate).replace('.', ',').replace(',', '.', 1))
      except ModelError as error:
         print(error)

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()