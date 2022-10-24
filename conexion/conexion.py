import mariadb

class Conexion:

    def conectarOpen(self):
        # Conexion a Base de datos OPEN GTS
        try:
            conexion = mariadb.connect(user="gts",password="opengts",host="192.168.102.105",database="gts") 
            print(
                '########################################\n# Conexion a base de datos establecida #\n########################################\n')
            return conexion
        except mariadb.Error as e:
          print("No se puedo conectar a la base de datos !")
          print("Error: {}".format(e))
        #cursor = conexion.cursor()