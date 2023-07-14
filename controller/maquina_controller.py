import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from model.maquina import Maquina
from controller.productos_controller import ProductoController
from controller.ventas_controller import VentasController

class MaquinaController:
    def __init__(self):
        self.__maquina = Maquina(0)

    def agregarSaldo(self,monto):
        if (monto):
            saldo_actual = self.__maquina.getSaldo()
            saldo_posterior = saldo_actual+monto
            self.__maquina.setSaldo(saldo_posterior)
            return print('cambio realizado')
        else:
            return 'error en el monto'
        
    def modificarSaldo(self,producto,cantidad):
        saldo_actual = self.__maquina.getSaldo()
        precio_producto = producto.getPrecio()*cantidad
        if saldo_actual >= precio_producto:
            saldo_posterior = saldo_actual - precio_producto
            self.__maquina.setSaldo(saldo_posterior) 
            return print('el saldo a sido modificado')
        else:
            return 'el saldo es inferior al producto'
    def saldoActual(self):
        return self.__maquina.getSaldo()
    
    def dineroAdmitido(self):
        return self.__maquina.getDineroAdmitido()
        
    def comprobarString(self,caracter):
        if type(caracter) == str:
            return True
        else:
            return False
        


