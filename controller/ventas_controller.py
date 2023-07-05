import sys
import os
from datetime import datetime
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from model.venta import Venta

class VentasController:
    def __init__(self):
        self.__venta = Venta(None,None,None,None,None)
    def agregarVenta(self, producto, cantidad,):
        if type(producto.getId() == int and producto.getPrecio() == int):
            total = producto.getPrecio() * int(cantidad)
            venta = Venta(0,producto.getId(),datetime.now(), int(cantidad), total)
            self.__venta.agregarVenta(venta)
            return print('venta agregada')
        else:
            return print('error en los datos ingresados')
    def verVenta(self):
        return self.__venta.verVentas()
    