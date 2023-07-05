import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from controller.ventas_controller import VentasController

class VentasView:
    def __init__(self):
        pass
    def ventasView(self,ventas):
        if len(ventas) != 0:
            for x in ventas:
                print("id venta: " + str(x.getId()))
                print("Producto id: " + str(x.getProducto()))
                print("Fecha venta: " + str(x.getFechaVenta()))
                print("Cantidad: " + str(x.getCantidad()))
                print("Total: " + str(x.getTotal()))
                print()
            d = input("\nOprime ENTER para continuar ...")
    