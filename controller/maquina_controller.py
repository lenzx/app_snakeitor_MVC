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
        self.__productoController = ProductoController()
        self.__ventaController = VentasController()

    def agregarSaldo(self,monto):
        if (monto):
            saldo_actual = self.__maquina.getSaldo()
            saldo_posterior = saldo_actual+monto
            self.__maquina.setSaldo(saldo_posterior)
            return print('cambio realizado')
        else:
            return 'error en el monto'
    def verProductos(self):
        return self.__productoController.verProductos()
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
        
    def comprobarInt(self, numero):
        if numero.isnumeric():
            return True
        else:
            return False
        
    def existeOpcion(self,opcion,productos):
        try:
            productos[int(opcion)-1]
            return True
        except:
            return False
    def realizarCompra(self,opcion,cantidad,productos):
        productoSelecionado = productos[int(opcion)-1]
        print(productoSelecionado.getNombre(),productoSelecionado.getStock())
        nuevo_Stock = productoSelecionado.getStock()-int(cantidad)
        productoSelecionado.setStock(nuevo_Stock)
        self.modificarSaldo(productoSelecionado,cantidad)
        self.__productoController.actualizarProductos(productoSelecionado.getId(),productoSelecionado.getNombre(),productoSelecionado.getPrecio(),productoSelecionado.getStock())
        self.__ventaController.agregarVenta(productoSelecionado,cantidad)



