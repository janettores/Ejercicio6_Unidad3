from claseUsado import Usado
from claseNuevo import Nuevo


class menuOpciones:
    __opcion: int

    def __init__(self):
        self.__opcion = 0

    def opciones(self, manejadorVehiculos):

        while self.__opcion != 8:
            print("Menu de Opciones")
            print("1)- Insertar un vehiculo en una posicion determinada")
            print("2)- Agregar un vehiculo a la coleccion")
            print(
                "3)- Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
            print(
                "4)- Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
            print("5)- Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
            print(
                "6)- Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
            print("7)- Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.")
            print("8)- SALIR")
            self.__opcion = int(input("\nIngrese una opcion: "))

            if self.__opcion == 1:

                tipo = str(input("Que vehiculo desea ingresar 'U': usado, 'N': nuevo: "))

                marca = str(input("Ingrese la marca: "))
                modelo = str(input("Ingrese el modelo: "))
                puertas = int(input("Ingrese la cantidad de puertas: "))
                color = str(input("Ingrese el color: "))
                precio = int(input("Ingrese el precio base: "))
                if tipo == 'U' or tipo == 'u':
                    patente = str(input("Ingrese la patente: "))
                    anio = int(input("Ingrese el anio: "))
                    kms = int(input("Ingrese el kilometraje: "))
                    vehiculo = Usado(marca, modelo, puertas, color, precio, patente, anio, kms)

                elif tipo == 'N' or tipo == 'n':

                    version = str(input("Ingrese la version del vehiculo (base o full):"))
                    vehiculo = Nuevo(marca, modelo, puertas, color, precio, version)

                posicion = int(input("Ingrese una posicion de la lista para insertar el vehiculo: "))
                manejadorVehiculos.insertarElemento(self, vehiculo, posicion)

            elif self.__opcion == 2:
                tipo = str(input("Que vehiculo desea ingresar 'U': usado, 'N': nuevo: "))

                marca = str(input("Ingrese la marca: "))
                modelo = str(input("Ingrese el modelo: "))
                puertas = int(input("Ingrese la cantidad de puertas: "))
                color = str(input("Ingrese el color: "))
                precio = int(input("Ingrese el precio base: "))
                if tipo == 'U' or tipo == 'u':
                    patente = str(input("Ingrese la patente: "))
                    anio = int(input("Ingrese el anio: "))
                    kms = int(input("Ingrese el kilometraje: "))
                    vehiculo = Usado(marca, modelo, puertas, color, precio, patente, anio, kms)

                elif tipo == 'N' or tipo == 'n':

                    version = str(input("Ingrese la version del vehiculo (base o full):"))
                    vehiculo = Nuevo(marca, modelo, puertas, color, precio, version)

                manejadorVehiculos.agregarElemento(vehiculo)

            elif self.__opcion == 3:
                posicion = int(input("Ingrese una posicion de la lista para mostrar el tipo de vehiculo: "))
                manejadorVehiculos.mostrarElemento(posicion)

            elif self.__opcion == 4:
                ingpat = str(input("Ingrese una patente de un vehiculo usado: "))
                band = manejadorVehiculos.existePatente(ingpat)
                if band == False:
                    print("La patente ingresada no existe")
                else:
                    nuevoprecio = float(input("Ingrese el nuevo precio base del vehiculo: "))
                    manejadorVehiculos.modificaPrecio(ingpat, nuevoprecio)
                    manejadorVehiculos.mostrarValor(ingpat)

            elif self.__opcion == 5:
                print("Vehiculo mas economico: ")
                manejadorVehiculos.masEconomico()

            elif self.__opcion == 6:
                print("Modelo\t\tCantidad de Puertas\t\tImporte de venta")
                manejadorVehiculos.vehiculosConcesionaria()

            elif self.__opcion == 7:
                manejadorVehiculos.toJSON()



            elif self.__opcion == 8:
                print("FIN DEL PROGRAMA")

            else:
                print("Opcion incorrecta, ingrese otra opcion ")