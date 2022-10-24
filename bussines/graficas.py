import matplotlib.pyplot as plt
from conexion.conexion import Conexion

conexion = Conexion().conectarOpen()
cursor = conexion.cursor()

class Graficas:
	def consulta(self,accountID,deviceID,fechaIni,fechaFin):
		print(accountID + " / " +  deviceID +" / "+ fechaIni + " / " + fechaFin )
		Sql = " SELECT  r.description as descripcion, count(r.description) as Cantidad from NotifyQueue nq left join Rule r on (r.ruleID=nq.ruleID) where nq.accountID= '"+accountID+"' and nq.deviceID='"+deviceID+"'  and timestamp >= (UNIX_TIMESTAMP('"+fechaIni+"'))   and timestamp <= (UNIX_TIMESTAMP('"+fechaFin+"'))  GROUP by r.description order by timestamp;"
		print(Sql)
		cursor.execute(Sql)
		eje_x = []
		eje_y = []
		for descripcion, Cantidad in cursor:
			eje_x.append(descripcion)
			eje_y.append(Cantidad)
		print(eje_x)
		print(eje_y)
		cursor.close()
		self.construirGrafica(eje_x,eje_y)
		return eje_x

	def construirGrafica(self,eje_x,eje_y):
		plt.legend()
		plt.barh(eje_x, eje_y)
		plt.title('Tabla de alertas')
		plt.savefig("img/output.jpg")
		plt.show()

