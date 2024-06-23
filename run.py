from app.controllers.homeController import homeController
from app.views.loginView import login
from app.views.registerView import register
from app.controllers.sucursalController import createPaquete, sucursalController
from app.controllers.sucursalController import sucursalNumController
from app.controllers.transporteController import transporteController
from app.views.sucursalView import sucursal
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
@app.route("/transportes")
def transportes():
    return transporteController()
@app.route("/sucursales/<id>")
def sucursalNum(id):
    return sucursalNumController(id)
@app.route("/sucursales/<id>/regPaquete",methods=['POST'])
def registerPaq(id):
    return createPaquete(id)
if __name__ =="__main__":
    
    app.run()