import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from database.database import DB

class Venta(DB):
    def __init__(self,id,producto,fecha_venta,cantidad,total):
        super().__init__()
        self.__id = id
        self.__producto = producto
        self.__fechaVenta = fecha_venta
        self.__cantidad = cantidad
        self.__total = total
    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
    def getProducto(self):
        return self.__producto
    def getFechaVenta(self):
        return self.__fechaVenta
    def getCantidad(self):
        return self.__cantidad
    def getTotal(self):
        return self.__total
    def setProducto(self,newProducto):
        self.__producto = newProducto
    def setFechaVenta(self,newFechaVenta):
        self.__fechaVenta = newFechaVenta
    def setCantidad(self,newcantidad):
        self.__cantidad = newcantidad
    def setTotal(self,newTotal):
        self.__total = newTotal

    def agregarVenta(self,venta):
        val = (venta.getProducto(),venta.getFechaVenta(),venta.getCantidad(),venta.getTotal())
        sql = "INSERT INTO ventas (producto_id, fecha_venta, cantidad, total) VALUES (%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el costo de habitacion a sido agregado')
        except Exception as e:
            print("Error: ", e.args)

    def verVentas(self):
        ventas = []
        sql = "SELECT * FROM ventas ORDER BY id asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    venta = Venta(x[0],x[1],x[2],x[3],x[4])
                    ventas.append(venta)
                return ventas
            else:
                print("No hay habitacion en la base de datos")
        except Exception as e:
            print("Error: ", e.args)
    
    def actualizarVentas(self,venta):
        val = (venta.getProducto(),venta.getFechaVenta(),venta.getCantidad(),venta.getTotal(),venta.getId())
        sql = "UPDATE ventas SET producto_id = %s, fecha_venta = %s, cantidad = %s, total = %s WHERE id = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)
    
    def eliminarVenta(self,venta):
        val= venta.getId()
        sql = "DELETE FROM ventas WHERE id = %s;"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

