import requests

#Invocar al metodo get con la url especifica
r = requests.get('https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey=C666B578-CE6A-40FD-B738-F249F7F5E26A')

print("codigo http resupuesta",r.status_code)

print("Cabecera",r.headers['content-type'])

print("encoding:",r.encoding)

print("Respuesta en string",r.text)
print(type(r.text))

print("Respuesta en json:",r.json())
print(type(r.text))
