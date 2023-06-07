import json
from pathlib import Path

from claseLista import Lista
from claseNodo import Nodo
from claseNuevo import Nuevo
from claseUsado import Usado


class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                listaVehiculos = class_()
                vehiculos = d['vehiculos']
                for i in range(len(vehiculos)):
                    dvehic = vehiculos[i]
                    class_name = dvehic.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dvehic["__atributos__"]
                    unVehic = class_(**atributos)
                    listaVehiculos.agregarVehiculo(unVehic)
            return listaVehiculos

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino: json.dump(diccionario, destino, indent=4)
        destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente: diccionario = json.load(fuente)
        fuente.close()
        return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)