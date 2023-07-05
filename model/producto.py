import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from database.database import DB

class Producto(DB):
    def __init__(self,id,nombre,precio,stock):
        super().__init__()
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock =stock
    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    def getStock(self):
        return self.__stock
    def setNombre(self, nombre):
        self.__nombre =nombre
    def setPrecio(self, precio):
        self.__precio = precio
    def setStock(self, stock):
        self.__stock = stock

    def agregarProducto(self,producto):
        val = (producto.getNombre(),producto.getPrecio(),producto.getStock())
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el costo de habitacion a sido agregado')
        except Exception as e:
            print("Error: ", e.args)

    def verProductos(self):
        productos = []
        sql = "SELECT * FROM productos WHERE stock > 0 ORDER BY id asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    producto = Producto(x[0],x[1],x[2],x[3])
                    productos.append(producto)
                return productos
            else:
                print("No hay habitacion en la base de datos")
        except Exception as e:
            print("Error: ", e.args)
            d = input('asdasddsadas')
    
    def actualizarProducto(self,producto):
        val = (producto.getNombre(),producto.getPrecio(), producto.getStock(),producto.getId(),)
        sql = "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)
    
    def eliminarProducto(self,producto):
        val= producto.getId()
        sql = "DELETE FROM productos WHERE id = %s;"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)
