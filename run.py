from flask import Flask
from app.views.homeView import home
from app import createApp
app = createApp()
@app.route("/")
def saludo():
    return home()
if __name__ =="__main__":
    app.run()