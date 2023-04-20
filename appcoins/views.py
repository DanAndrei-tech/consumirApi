
class Views:
  
  def InsertCoin(self):
      crypto = input("Ingrese moneda digital").upper()
      return crypto
  
  def viewListCoins(self,allcoin):
      print (f"La cantidad de criptos son: {len(allcoin.lista_criptos)},\
       y la cantidad de no criptos son: {len(allcoin.lista_no_criptos)}")

    
  def viewRateExchange(self,change):
      print("{:,.2f}€".format(change.rate).replace('.', ',').replace(',', '.', 1))

  def viewError(self,err):
      print(err)