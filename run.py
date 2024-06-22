from flask import Flask
from app.views.homeView import home
from app.views.loginView import login
from app.views.registerView import register
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

if __name__ =="__main__":
    app.run()