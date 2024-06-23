from flask import Flask
from app.views.homeView import home
from app.views.loginView import login
from app.views.registerView import register
from app.views.sucursalView import sucursales
from app.views.sucursalView import sucursal
from app import createApp
app = createApp()
@app.route("/")
def saludo():
    return home()
@app.route("/login")
def log():
    return login()
@app.route("/register")
def reg():
    return register()
@app.route("/sucursales")
def sucu():
    return sucursales()
@app.route("/sucursales/<num>")
def sucursalNum(num):
    return sucursal(num)
if __name__ =="__main__":
    app.run()