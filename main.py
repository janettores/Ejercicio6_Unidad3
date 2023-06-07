from claseManejador import manejadorVehiculos
from menu import menuOpciones

if __name__ == '__main__':

    manejador = manejadorVehiculos()
    manejador.cargarLista()
    menu = menuOpciones()
    menu.opciones(manejador)