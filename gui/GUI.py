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
from controller.main_controller import MainController

class Interfaz:
    def __init__(self):
        self.__maquinaView = MaquinaView()
        self.__productoView = ProductoView()
        self.__ventaView = VentasView()
        self.__mainController = MainController()
        self.inicia()

    def menuUsuario(self):
        productos = self.__mainController.verProductos()
        saldo_actual = self.__mainController.verSaldo()
        dinero_admitido = self.__mainController.verDineroAdmitido()
        self.__maquinaView.tituloView()
        self.__productoView.productosDisponibles(productos,saldo_actual)
        self.__maquinaView.saldoView(saldo_actual)
        self.__maquinaView.dineroAdmitidoView(dinero_admitido)
        self.__maquinaView.opcionesView(productos)

    def menuAdmin(self):
        self.__maquinaView.opcionesAdmin()

    def inicia(self):
        opcion = True
        while(opcion):
            os.system('cls')
            self.menuUsuario()
            op = input("N Opcion / $dinero: ")
            opcion1 = True
            if (self.__mainController.comprobarInt(op)):
                if (self.__mainController.existeOpcion(op)):
                    os.system('cls')
                    cantidad = int(input('seleccione la cantidad a comprar: '))
                    self.__mainController.realizarCompra(op,cantidad)
                    d = input("\nOprime ENTER para continuar ...")

                elif (int(op) in self.__mainController.verDineroAdmitido()):
                    os.system('cls')
                    self.__mainController.agregarSaldo(int(op))
                    d = input("\nOprime ENTER para continuar ...")

                elif int(op) == 9090:
                    while opcion1:
                        opcion2 = True
                        os.system('cls')
                        usuario = str(input('ingrese su usuario: '))
                        password = str(input('ingrese su contraseña: '))
                        if(self.__mainController.verificarUsuario(usuario,password)):
                            while opcion2:
                                os.system('cls')
                                self.menuAdmin()
                                op = input("N Opcion: ")
                                if (self.__mainController.comprobarInt(op)):
                                    if int(op) == 1:
                                        os.system('cls')
                                        nombre = str(input('ingrese el nombre del producto'))
                                        precio = int(input('ingrese el precio del producto'))
                                        stock = int(input('ingrese el stock del producto'))
                                        self.__mainController.agregarProducto(nombre,precio,stock)
                                        d = input("\nOprime ENTER para continuar ...")
                                    elif int(op) == 2:
                                        os.system('cls')
                                        self.__ventaView.ventasView(self.__mainController.verProductos())

                                    elif int(op) == 3:
                                        os.system('cls')
                                        self.__productoView.productosView(self.__mainController.verVentas())
                                    elif int(op) == 4:
                                        os.system('cls')
                                        new_usuario = input('nombre de usuario')
                                        new_paswword = input('paswword')
                                        self.__mainController.agregarUsuario(new_usuario,new_paswword)

                                
                                else: 
                                    opcion1 = False
                                    opcion2 = False
                        else:
                            os.system('cls')
                            print('usuario o contraseña erroneo')
                            print('pulse cualquier letra para continuar')
                            print('escriba exit para salir')
                            d = input("")
                            if d == "exit":
                                opcion1 = False

                else:
                    os.system('cls')
                    print('ingrese una opcion valida')
                    d = input("\nOprime ENTER para continuar ...")
            else:
                os.system('cls')
                print('ingrese una opcion valida')
                d = input("\nOprime ENTER para continuar ...")
            

interfaz = Interfaz()