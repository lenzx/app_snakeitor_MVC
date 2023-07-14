import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from database.database import DB

class Usuario(DB):
    def __init__(self,id,usuario,password):
        super().__init__()
        self.__id = id
        self.__usuario = usuario
        self.__password = password

    def getId(self):
        return self.__id
    def getUsuario(self):
        return self.__usuario
    def getPassword(self):
        return self.__password
    def setId(self,newId):
        self.__id = newId
    def setUsuario(self, newUsuario):
        self.__usuario = newUsuario
    def setPassword(self, newPassword):
        self.__password = newPassword
        
    def agregarUsuario(self,usuario):
        val = (usuario.getUsuario(),usuario.getPassword())
        sql = "INSERT INTO usuario (user, password) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el usuario a sido agregado')
        except Exception as e:
            
            print("Error: ", e.args)

    def verUsuario(self):
        usuarios = []
        sql = "SELECT * FROM usuario ORDER BY id asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    usuario = Usuario(x[0],x[1],x[2])
                    usuarios.append(usuario)
                return usuarios
            else:
                print("No hay usuarios en la base de datos")
        except Exception as e:
            print("Error: ", e.args)

    def verUsuarioId(self,id):
        val=id
        sql = "SELECT * FROM usuario WHERE id = %s"
        try:
            self.cursor.execute(sql,val)
            datos = self.cursor.fetchone()
            if (len(datos) != 0):
                usuario = Usuario(datos[0],datos[1],datos[2])
                return usuario
            else:
                print("No hay usuarios en la base de datos")
        except Exception as e:
            print("Error: ", e.args)
    
    def actualizarUsuario(self,usuario):
        val = (usuario.getUsuario(),usuario.getPassword(),usuario.getId())
        sql = "UPDATE usuario SET user = %s, password = %s WHERE id = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)
    
    def eliminarUsuario(self,usuario):
        val= usuario.getId()
        sql = "DELETE FROM usuario WHERE id = %s;"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('usuario eliminado')
        except Exception as e:
            print("Error: ", e.args)
