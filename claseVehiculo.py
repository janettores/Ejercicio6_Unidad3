class Vehiculo:
    __modelo: str
    __cantidadpuertas: int
    __color: str
    __preciobase: float
    __marca: str

    def __init__(self, modelo='', puertas=0, color='', preciobase=0, marca=''):
        self.__modelo = modelo
        self.__cantidadpuertas = puertas
        self.__color = color
        self.__preciobase = preciobase
        self.__marca = marca

    def getModelo(self):
        return self.__modelo

    def getCantidadPuertas(self):
        return self.__cantidadpuertas

    def getColor(self):
        return self.__color

    def getPrecioBase(self):
        return self.__preciobase

    def getMarca(self):
        return self.__marca

    def cambiarPrecio(self, nuevoprecio):
        self.__preciobase = nuevoprecio

    def __str__(self):
        return self.__marca + " " + self.__modelo + " " + self.__color + " " + str(
            self.__cantidadpuertas) + " Puertas\tPrecio base:" + str(self.__preciobase)