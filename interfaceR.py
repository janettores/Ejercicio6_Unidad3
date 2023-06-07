from zope.interface import Interface


class IVehiculo(Interface):

    def insertarVehiculo(posicion):
        pass

    def agregarVehiculo(vehiculo):
        pass

    def mostrarVehiculo(posicion):
        pass