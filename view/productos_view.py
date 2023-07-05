import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from controller.productos_controller import ProductoController
from controller.maquina_controller import MaquinaController

class ProductoView:
    def __init__(self) -> None:
        pass

    def productosView(self,productos):
        for x in productos:
            print("id: " + str(x.getId()))
            print("Nombre: " + str(x.getNombre()))
            print("Precio: " + str(x.getPrecio()))
            print("Stock: " + str(x.getStock()))
            print()
        d = input("\nOprime ENTER para continuar ...")

    def productosDisponibles(self,productos,saldo):
        cadena =''
        for i in productos:
            if (saldo >= i.getPrecio()):
                cadena = cadena + ("[ "+ str(productos.index(i)+1)+" ] [x] ").ljust(10," ")+(i.getNombre()).ljust(53," ")+"$ "+str(i.getPrecio())+'  '+str(i.getStock())+ "\n"
            else:
                cadena = cadena + ("[ "+ str(productos.index(i)+1)+" ] [-] ").ljust(10," ")+(i.getNombre()).ljust(53," ")+"$ "+str(i.getPrecio())+'  '+str(i.getStock())+ "\n"
        print(cadena)

