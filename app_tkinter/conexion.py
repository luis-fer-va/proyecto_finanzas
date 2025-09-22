#Conexión a mysql
import pymysql

class ConexionDB:
    def __init__(self):
        self.connection=pymysql.connect(
        host='localhost',user='root',password='Alancito123',database='finanzas')
        self.cursor=self.connection.cursor()
        print('conexion establecida')

    def cerrar(self):
        self.connection.commit()
        self.connection.close()
