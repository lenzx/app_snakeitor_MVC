import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from controller.maquina_controller import MaquinaController
from controller.productos_controller import ProductoController

class MaquinaView:
    def __init__(self):
        pass
    
    def tituloView(self):
        print (" S-N-A-C-K-E-I-T-O-R ".center(70, "#"))
        print(" ")
        print ("=".center(70,"="))
        print(" Ofertas del día ".center(70," "))

    def saldoView(self,saldo):
        print ("=".center(70,"="))
        print("ingrese dinero para comprar productos")
        print("su saldo actual es de: "+ str(saldo))

    def dineroAdmitidoView(self,dineroAdmitido):
        print ("=".center(70,"="))
        cadena = "ingrese solo: "
        for i in dineroAdmitido:
            cadena = cadena +"$" +str(i)+"-"
        print (cadena.rstrip(cadena[-1]))

    def opcionesView(self,opciones):
        cadena = "ingrese opciones de producto: "
        for i in opciones:
            cadena = cadena + str(opciones.index(i)+1) + "-"
        print(cadena.rstrip(cadena[-1]))

    def opcionesAdmin(self):
        self.tituloView()
        print('[ 1 ] Agregar Producto')
        print('[ 2 ] Ver productos')
        print('[ 3 ] Ver ventas')
