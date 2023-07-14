import sys
import os
from werkzeug.security import generate_password_hash, check_password_hash
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from model.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.__usuario = Usuario(None,None,None)
    
    def agregarUsuario(self,user,password):
        pass_encriptado = generate_password_hash(password)
        usuario = Usuario(None,user,pass_encriptado)
        self.__usuario.agregarUsuario(usuario)
    
    def verUsuario(self):
        return self.__usuario.verUsuario()
    
    def verUsuarioId(self,id):
        usuario = self.__usuario.verUsuarioId(id)
        return usuario

    def modificarUsuario(self,user,password,newUser,newPassword):
        usuarios = self.verUsuario()
        for x in usuarios:
            if (x.getUsuario() == user and x.getPassword() ==password ):
                x.setUsuario(newUser)
                x.setPassword(newPassword)
                self.__usuario.actualizarUsuario(x)

    def eliminarUsuario(self,id):
        usuario = self.verUsuarioId(id)
        self.__usuario.eliminarUsuario(usuario)