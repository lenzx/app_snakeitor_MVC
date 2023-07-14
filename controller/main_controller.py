import sys
import os
from werkzeug.security import generate_password_hash, check_password_hash


# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from controller.maquina_controller import MaquinaController
from controller.productos_controller import ProductoController
from controller.ventas_controller import VentasController
from controller.usuario_controller import UsuarioController

class MainController:
    def __init__(self):
        self.__maquinaController = MaquinaController()
        self.__productoController = ProductoController()
        self.__ventaController = VentasController()
        self.__usuarioController = UsuarioController()
    
    def verProductos(self):
        productos = self.__productoController.verProductos()
        return productos
    def verVentas(self):
        ventas = self.__ventaController.verVenta()
        return ventas
    def verUsuario(self):
        usuarios = self.__usuarioController.verUsuario()
        return usuarios
    def verSaldo(self):
        saldo_actual = self.__maquinaController.saldoActual()
        return saldo_actual
    def agregarSaldo(self,monto):
        self.__maquinaController.agregarSaldo(monto)
    def verDineroAdmitido(self):
        dinero_admitido = self.__maquinaController.dineroAdmitido()
        return dinero_admitido
    def existeOpcion(self,opcion):
        productos = self.__productoController.verProductos()
        try:
            productos[int(opcion)-1]
            return True
        except:
            return False
    def comprobarInt(self, numero):
        if numero.isnumeric():
            return True
        else:
            return False
    def realizarCompra(self,opcion,cantidad):
        productos = self.__productoController.verProductos()
        productoSelecionado = productos[int(opcion)-1]
        nuevo_Stock = productoSelecionado.getStock()-cantidad
        productoSelecionado.setStock(nuevo_Stock)
        self.__maquinaController.modificarSaldo(productoSelecionado,cantidad)
        self.__productoController.actualizarProductos(productoSelecionado.getId(),productoSelecionado.getNombre(),productoSelecionado.getPrecio(),productoSelecionado.getStock())
        self.__ventaController.agregarVenta(productoSelecionado,cantidad)
    def verificarUsuario(self,usuario,password):
        usuarios = self.__usuarioController.verUsuario()
        for x in usuarios:
            if (x.getUsuario()==usuario and check_password_hash(x.getPassword(),password)):
                return True
        return False
    
    def agregarProducto(self,nombre,precio,stock):
        self.__productoController.agregarProducto(nombre,precio,stock)

    def agregarUsuario(self,usuario,password):
        nuevo_usuario = self.__usuarioController.agregarUsuario(usuario,password)
    
