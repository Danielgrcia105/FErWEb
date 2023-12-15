from zeep import Client 

wsdl = 'http://www.SoapClient.com/xml/SoapResponder.wsdl'
if Client :
    cliente = Client (wsdl= wsdl)
    result = cliente.wsdl
    print(cliente.service.Method1('Lean', 'is Very Cute in program whit python<3'))
    
else:
    print("No fue posible conectarse con el servicio")