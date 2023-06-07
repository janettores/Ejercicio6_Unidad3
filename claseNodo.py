from claseUsado import Usado
from claseNuevo import Nuevo


class Nodo:
    __vehiculo: object
    __siguiente: object

    def __init__(self, vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__vehiculo

    def getPat(self):
        if isinstance(self.__vehiculo, Usado):
            return self.__vehiculo.getPatente()
        else:
            return False

    def getTipo(self):

        if isinstance(self.__vehiculo, Usado):
            print("Auto Usado\n")

        elif isinstance(self.__vehiculo, Nuevo):
            print("Auto Nuevo\n")

    def modificadorPrecio(self, nuevoprecio):
        if isinstance(self.__vehiculo, Usado):
            self.__vehiculo.cambiarPrecio(nuevoprecio)
        else:
            return False

    def obtenerValor(self):
        return self.__vehiculo.importeVenta()

    def datosConcesionaria(self):
        print("{}\t\t\t{}\t\t\t    ${}".format(self.__vehiculo.getModelo(), self.__vehiculo.getCantidadPuertas(),
                                               self.__vehiculo.importeVenta()))

    def toJSON(self):
        if isinstance(self.__vehiculo, Usado):
            d = dict(__class__="Usado",
                     __atributos__=dict(marca=self.__vehiculo.getMarca(), modelo=self.__vehiculo.getModelo(),
                                        cantidadpuertas=self.__vehiculo.getCantidadPuertas(),
                                        color=self.__vehiculo.getColor(), preciobase=self.__vehiculo.getPrecioBase(),
                                        patente=self.__vehiculo.getPatente(), anio=self.__vehiculo.getAnio(),
                                        kilometraje=self.__vehiculo.getKilometraje()))
        elif isinstance(self.__vehiculo, Nuevo):
            d = dict(__class__="Nuevo",
                     __atributos__=dict(marca=self.__vehiculo.getMarca(), modelo=self.__vehiculo.getModelo(),
                                        cantidadpuertas=self.__vehiculo.getCantidadPuertas(),
                                        color=self.__vehiculo.getColor(), preciobase=self.__vehiculo.getPrecioBase(),
                                        version=self.__vehiculo.getVersion()))

        return d