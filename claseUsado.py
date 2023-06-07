from claseVehiculo import Vehiculo

class Usado(Vehiculo):
    __patente: str
    __anio: int
    __kilometraje: int

    def __init__(self, modelo='', puertas=0, color='', preciobase=0, marca='', patente='', anio=0, kilometraje=0):
        super().__init__(modelo, puertas, color, preciobase, marca)
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = kilometraje

    def getPatente(self):
        return self.__patente

    def getAnio(self):
        return self.__anio

    def getKilometraje(self):
        return self.__kilometraje

    def importeVenta(self):
        precioventa = super().getPrecioBase() - (super().getPrecioBase() * (1 * (2023 - self.__anio))) / 100
        if self.__kilometraje > 100000:
            restar = super().getPrecioBase() * (2 / 100)
            precioventa -= restar

        return precioventa

    def __str__(self):
        return super().__str__() + "\nPatente: " + self.__patente + " Año: " + str(
            self.__anio) + " Kilometraje: " + str(self.__kilometraje)