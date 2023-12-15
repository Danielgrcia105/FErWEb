from zeep import Client
 
service_url = 'http://www.dneonline.com/calculator.asmx?WSDL'
 
 
if Client:
 # Inicio del soap en cliente
 client = Client(service_url)
 result = client.service.Add(665,1)
 print("Resultado: {}".format(result))
 
 
else:
    print('Numnero no encontrado')