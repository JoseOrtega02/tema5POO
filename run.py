from app.controllers.homeController import homeController
from app.controllers.paqueteController import asignarPaqueteController
from app.controllers.repartidorController import entregaPaqueteController, loginRepartidorController, repartidorController
from app.controllers.sucursalController import createPaquete, sucursalController
from app.controllers.sucursalController import sucursalNumController
from app.controllers.transporteController import salidaTransporteController, llegadaTransporteConreoller
from app.controllers.transporteController import seleccionarPaquetesController
from app import createApp
from app.views.repartidorView import repartidorView
app = createApp()
#home
@app.route("/")
def saludo():
    return homeController()
#funcionalidad 6
@app.route("/loginRepartidor",methods=['GET',"POST"])
def log():
    return loginRepartidorController()
#funcionalidad 7
@app.route("/repartidor/<id>",methods=['GET',"POST"])
def repartidor(id):
    return repartidorController(id)
@app.route("/registrarEntrega/<id>",methods=['GET',"POST"])
def registrarEntrega(id):
    return entregaPaqueteController(id)
#func 1
@app.route("/sucursales")
def sucu():
    return sucursalController()
#func 4
@app.route("/transporteLlegada/<id>",methods=['GET',"POST"])
def transporteLlegada(id):
    return llegadaTransporteConreoller(id)
#func 1
@app.route("/sucursales/<id>")
def sucursalNum(id):
    return sucursalNumController(id)
#func 2
@app.route("/sucursales/<id>/regPaquete",methods=['POST'])
def registerPaq(id):
    return createPaquete(id)
#func 3
@app.route('/salidaTransporte/<int:id>', methods=['GET'])
def salidaTransporte(id):
    return salidaTransporteController(id)

#func 3
@app.route("/seleccionarPaquetes/<id>",methods=["GET","POST"])
def selecPaq(id):
    return seleccionarPaquetesController(id)
#func 5
@app.route("/asignarPaquetes/<id>",methods=["GET","POST"])
def asigPaq(id):
    return asignarPaqueteController(id)
if __name__ =="__main__":
    
    app.run()