from app.controllers.homeController import homeController
from app.views.loginView import login
from app.views.registerView import register
from app.controllers.sucursalController import createPaquete, sucursalController
from app.controllers.sucursalController import sucursalNumController
from app.controllers.transporteController import salidaTransporteController, llegadaTransporteConreoller
from app.views.sucursalView import sucursal
from app.controllers.transporteController import seleccionarPaquetesController
from app import createApp
app = createApp()
@app.route("/")
def saludo():
    return homeController()
@app.route("/login")
def log():
    return login()
@app.route("/register")
def reg():
    return register()
@app.route("/sucursales")
def sucu():
    return sucursalController()
@app.route("/transporteLlegada/<id>",methods=['GET',"POST"])
def transporteLlegada(id):
    return llegadaTransporteConreoller(id)
@app.route("/sucursales/<id>")
def sucursalNum(id):
    return sucursalNumController(id)
@app.route("/sucursales/<id>/regPaquete",methods=['POST'])
def registerPaq(id):
    return createPaquete(id)
@app.route('/salidaTransporte/<int:id>', methods=['GET'])
def salidaTransporte(id):
    return salidaTransporteController(id)
@app.route("/seleccionarPaquetes/<id>",methods=["GET","POST"])
def selecPaq(id):
    return seleccionarPaquetesController(id)
if __name__ =="__main__":
    
    app.run()