from claseVehiculo import Vehiculo


class Nuevo(Vehiculo):
    __version: str

    def __init__(self, modelo='', puertas=0, color='', preciobase=0, marca='', version=''):
        super().__init__(modelo, puertas, color, preciobase, marca)
        self.__version = version

    def getVersion(self):
        return self.__version

    def importeVenta(self):
        precioventa = super().getPrecioBase() + (super().getPrecioBase() * (10 / 100))
        if self.__version == 'full':
            sumar = super().getPrecioBase() * (2 / 100)
            precioventa += sumar
        return precioventa

    def __str__(self):
        return super().__str__() + "\nVersion: " + self.__version