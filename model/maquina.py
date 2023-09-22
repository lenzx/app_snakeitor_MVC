import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from database.database import DB




class Maquina(DB):
    def __init__(self,saldo,dinero_admitido = [50,100,500,1000,2000]):
        super().__init__()
        self.__saldo = saldo
        self.__dineroAdmitido = dinero_admitido
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self,Nsaldo):
        self.__saldo = Nsaldo
    def getDineroAdmitido(self):
        return self.__dineroAdmitido
    def setDineroAdmitido(self, nDineroAdmitido):
        self.__dineroAdmitido = nDineroAdmitido


