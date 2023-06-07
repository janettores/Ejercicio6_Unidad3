from zope.interface import implementer

from interfaceR import IVehiculo
from claseNodo import Nodo


@implementer(IVehiculo)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __indice: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def agregarVehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def listarDatosVehiculos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def insertarVehiculo(self, posicion, vehiculo):
        posicion -= 1
        nuevo = Nodo(vehiculo)
        contador = 0
        if self.__comienzo == None:
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        elif (contador == posicion):
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        else:
            p = self.__comienzo
            anterior = self.__comienzo
            while (p != None) and (posicion > contador):
                anterior = p
                p = p.getSiguiente()
                contador += 1
            anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(p)

    def mostrarVehiculo(self, posicion):
        contador = 0
        aux = self.__comienzo
        while aux != None and contador != posicion:
            aux = aux.getSiguiente()
            contador += 1
        if contador == posicion:
            aux.getTipo()

    def getTope(self):
        return self.__tope

    def bPatente(self, patente):
        aux = self.__comienzo
        band = False
        while aux != None and patente != aux.getPat():
            aux = aux.getSiguiente()

        if aux.getPat() == patente:
            band = True
        return band

    def modificarPrecio(self, patente, nuevoprecio):
        aux = self.__comienzo
        while aux != None and patente != aux.getPat():
            aux = aux.getSiguiente()

        if aux.getPat() == patente:
            aux.modificadorPrecio(nuevoprecio)

    def buscarValor(self, patente):
        aux = self.__comienzo
        while aux != None and patente != aux.getPat():
            aux = aux.getSiguiente()

        if aux != None:
            print("El nuevo precio de venta del vehiculo es: {}".format(aux.obtenerValor()))

    def buscarMasEconomico(self):
        aux = self.__comienzo
        min = 10000000000
        automin: Nodo()
        while aux != None:
            if aux.obtenerValor() < min:
                min = aux.obtenerValor()
                automin = aux
            aux = aux.getSiguiente()

        return automin

    def mostrarConcesionaria(self):
        aux = self.__comienzo
        while aux != None:
            aux.datosConcesionaria()
            aux = aux.getSiguiente()

    def toJSON(self):
        aux = self.__comienzo
        ld = []
        while aux != None:
            vdic = aux.toJSON()
            ld.append(vdic)
            aux = aux.getSiguiente()

        return ld

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato