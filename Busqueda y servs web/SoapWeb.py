from zeep import Client

cliente= Client('http://schemas.xmlsoap.org/wsdl/soap/')
#log
if cliente.service.login("Morales", "asd"):
    print("Credencial correcta")
else:
    print("Error en credenciales")

#pago
if cliente.service.procesarpago(5000,9000)>=0:
    print("Pago realizado")
    
else: 
    print("Dinero insuficiente")