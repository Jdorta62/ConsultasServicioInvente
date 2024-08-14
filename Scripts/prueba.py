from zeep import Client

# URL del WSDL del servicio web
wsdl = 'https://www.pap.hacienda.gob.es/invente2/Servicios/Salida/CatalogoInventeV02/wcfSalida_InventeV02.svc?wsdl'

# Crear un cliente SOAP usando la URL del WSDL
client = Client(wsdl=wsdl)

# Llamar al servicio CatalogoEntidades()
#for i in range(1, 20):
#    response = client.service.CatalogoEntidades_ConFiltros(CodComunidad=i, adscripcion=4)
#    print(f"Comunidad: {i}. Total: {response.Total}\n")

response = client.service.CatalogoEntidades_ConFiltros(NIF="G38528824")


# Verificar el tipo de CatalogoEntidades
print(response)
#print(dir(response.CatalogoEntidades))
#print(dir(response.CatalogoEntidades.Datos_Sencillos_Entidad))
#print(len(response.CatalogoEntidades.Datos_Sencillos_Entidad))
contador = 0
# Iterar sobre las entidades
