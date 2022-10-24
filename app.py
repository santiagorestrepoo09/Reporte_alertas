import argparse
from bussines.graficas import Graficas

# construct the argument parse and parse the arguments
##  EJECUCION DEL ARGUMENTO  
# 
#     python app.py --deviceID '867844000528060' --fechaIni '2022-03-12 17:33:00' --fechaFin '2022-03-15 17:14:00' --accountID 'mctsas'

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--accountID", required=True,	help="var accountID no fund !")
ap.add_argument("-i", "--deviceID", required=True,	help="var deviceID no fund !")
ap.add_argument("-j", "--fechaIni", required=True,	help="var fechaIni no fund !")
ap.add_argument("-k", "--fechaFin", required=True,	help="var fechaFin no fund !")
args = vars(ap.parse_args())

## VARIABLES GLOBALESS
accountID = args["accountID"]
deviceID = args["deviceID"]
fechaIni = args["fechaIni"]
fechaFin = args["fechaFin"]

class App:
  Graficas().consulta(accountID,deviceID,fechaIni,fechaFin)
  def Consultar_CantidadAlertas():
    print(accountID + " / " +  deviceID +" / "+ fechaIni + " / " + fechaFin )

