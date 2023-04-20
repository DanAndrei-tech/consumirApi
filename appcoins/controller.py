
from appcoins.models import *
from appcoins.views import Views
from appcoins.config import APIKEY

class AppCoinsController:
   
  def executeProgram(self):
    allcoin = AllCoinApiIO()
    viewTools = Views()

    #consulta de todas las monedas
    allcoin.getAllCoins(APIKEY)

    viewTools.viewListCoins(allcoin = allcoin)

    moneda_cripto = viewTools.InsertCoin()

    while moneda_cripto != "" and moneda_cripto.isalpha() == True:
        if moneda_cripto in allcoin.lista_criptos: 
          exchange = Exchange(moneda_cripto)

          try:
            exchange.updateExchange(APIKEY)
            viewTools.viewRateExchange(exchange)
          except ModelError as error:
            viewTools.viewError(error)

        moneda_cripto = viewTools.InsertCoin()