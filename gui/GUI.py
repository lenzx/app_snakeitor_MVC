import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
##vistas
from view.maquina_view import MaquinaView
from view.productos_view import ProductoView
from view.ventas_view import VentasView
##controladores
from controller.maquina_controller import MaquinaController
from controller.productos_controller import ProductoController
from controller.ventas_controller import VentasController
from model.producto import Producto

class Interfaz:
    def __init__(self):
        self.__maquinaView = MaquinaView()
        self.__productoView = ProductoView()
        self.__ventaView = VentasView()
        self.__maquinaController = MaquinaController()
        self.__productoController = ProductoController()
        self.__ventaController = VentasController()
        self.inicia()
    def menuUsuario(self,productos):
        self.__maquinaView.tituloView()
        self.__productoView.productosDisponibles(productos,self.__maquinaController.saldoActual())
        self.__maquinaView.saldoView(self.__maquinaController.saldoActual())
        self.__maquinaView.dineroAdmitidoView(self.__maquinaController.dineroAdmitido())
        self.__maquinaView.opcionesView(productos)
    def menuAdmin(self):
        self.__maquinaView.opcionesAdmin()

    def inicia(self):
        opcion = True
        while(opcion):
            os.system('cls')
            self.menuUsuario(self.__maquinaController.verProductos())
            op = input("N Opcion / $dinero: ")
            opcion1 = True
            if (self.__maquinaController.comprobarInt(op)):
                if (self.__maquinaController.existeOpcion(op,self.__maquinaController.verProductos())):
                    os.system('cls')
                    cantidad = int(input('seleccione la cantidad a comprar: '))
                    self.__maquinaController.realizarCompra(op,cantidad,self.__maquinaController.verProductos())
                    d = input("\nOprime ENTER para continuar ...")
                elif (int(op) in self.__maquinaController.dineroAdmitido()):
                    os.system('cls')
                    self.__maquinaController.agregarSaldo(int(op))
                    d = input("\nOprime ENTER para continuar ...")
                elif int(op) == 9090:
                    while opcion1:
                        os.system('cls')
                        self.menuAdmin()
                        op = input("N Opcion: ")
                        if (self.__maquinaController.comprobarInt(op)):
                            if int(op) == 1:
                                os.system('cls')
                                nombre = str(input('ingrese el nombre del producto'))
                                precio = int(input('ingrese el precio del producto'))
                                stock = int(input('ingrese el stock del producto'))
                                self.__productoController.agregarProducto(nombre,precio,stock)
                                d = input("\nOprime ENTER para continuar ...")
                            elif int(op) == 2:
                                os.system('cls')
                                self.__ventaView.ventasView(self.__ventaController.verVenta())

                            elif int(op) == 3:
                                os.system('cls')
                                self.__productoView.productosView(self.__productoController.verProductos())
                        
                        else: 
                            opcion1 = False

            else:
                print('ingrese una opcion valida')
                d = input("\nOprime ENTER para continuar ...")
            

interfaz = Interfaz()