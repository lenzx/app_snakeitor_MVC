import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from model.producto import Producto

class ProductoController:
    def __init__(self):
        self.__producto = Producto(None,None,None,None)
        
    def agregarProducto(self,nombre,precio,stock):
        if (self.comprobarString(nombre) and self.comprobarInt(precio) and self.comprobarInt(stock)):
            producto = Producto(0,nombre,precio,stock)
            self.__producto.agregarProducto(producto)
            return print('producto agregado')
        else:
            return print('error en los datos')
        
    def verProductos(self):
        productos = self.__producto.verProductos()
        return productos
    
    def actualizarProductos(self,id,nombre,precio,stock):
        if (self.comprobarInt(id),self.comprobarString(nombre),self.comprobarInt(precio),self.comprobarInt(stock)):
            producto = Producto(id,nombre,precio,stock)
            self.__producto.actualizarProducto(producto)
            return print('se actualizo correctamente')
        else:
            return print('error al actualizar datos')
        
    def  eliminarProducto(self,id):
        if (self.comprobarInt(id)):
            producto = Producto(id,None,None,None)
            if self.existeId(producto.getId()):
                self.__producto.eliminarProducto(producto)
                return print('se a eliminado correctamente')
            else:
                return print('el id no existe')
        else:
            return print('error en el id')

    def comprobarString(self,caracter):
        if type(caracter) == str:
            return True
        else:
            
            return False
        
    def comprobarInt(self, numero):
        if type(numero) == int:
            return True
        else:
            return False
    def existeId(self,id):
        productos = self.__producto.verProductos()
        for i in productos:
            if (i.getId() == id):
                return True
        return False