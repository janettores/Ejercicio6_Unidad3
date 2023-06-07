from zope.interface import implementer


from claseObjectEncoder import ObjectEncoder

from interfaceR import IVehiculo
from claseLista import Lista

from posicionInvalida import PosicionInvalidaException


@implementer(IVehiculo)
class manejadorVehiculos:
    __listaVehiculos: Lista()

    def __init__(self):
        self.__listaVehiculos = Lista()

    def cargarLista(self):
        jsonF = ObjectEncoder()
        diccionario = jsonF.leerJSONArchivo('vehiculos.json')
        self.__listaVehiculos = jsonF.decodificarDiccionario(diccionario)

    def agregarElemento(self, vehiculo):
        self.__listaVehiculos.agregarVehiculo(vehiculo)

    def insertarElemento(self, vehiculo, posicion):
        if posicion < 0 or posicion > self.__listaVehiculos.getTope():
            raise PosicionInvalidaException("La posicion no es valida ")
        else:
            self.__listaVehiculos.insertarVehiculo(posicion, vehiculo)

    def mostrarElemento(self, posicion):
        self.__listaVehiculos.mostrarVehiculo(posicion)

    def listarDatos(self):
        self.__listaVehiculos.listarDatosVehiculos()

    def existePatente(self, patente):
        band = self.__listaVehiculos.bPatente(patente)
        return band

    def modificaPrecio(self, patente, nuevoprecio):
        self.__listaVehiculos.modificarPrecio(patente, nuevoprecio)

    def mostrarValor(self, patente):
        self.__listaVehiculos.buscarValor(patente)

    def masEconomico(self):
        autoEconomico = self.__listaVehiculos.buscarMasEconomico()
        print("{} \nsu precio de venta es: {}".format(autoEconomico.getDato(), autoEconomico.obtenerValor()))

    def vehiculosConcesionaria(self):
        self.__listaVehiculos.mostrarConcesionaria()

    def toJSON(self):
        jsonF = ObjectEncoder()
        d = self.__listaVehiculos.toJSON()
        jsonF.guardarJSONArchivo(d, "test.json")