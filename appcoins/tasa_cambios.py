import requests

apikey = 'C666B578-CE6A-40FD-B738-F249F7F5E26A'
#creo un input para cargar la moneda digital
moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:
    

  #Invocar al metodo get con la url especifica
  r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}')

  respuesta = r.json()
  #ejercicio 1, como capturamos el rate



  #ejercicio 2, como capturar el error
  if r.status_code == 200:
      print("{:,.2f}€".format(respuesta['rate']))
      break
  else:
      print(respuesta['error'])

  moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()













'''
print("codigo http resupuesta",r.status_code)

print("Cabecera",r.headers['content-type'])

print("encoding:",r.encoding)

print("Respuesta en string",r.text)
print(type(r.text))

print("Respuesta en json:",r.json())
print(type(r.json()))

'''


