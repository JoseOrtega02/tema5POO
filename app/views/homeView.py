from flask import render_template
from app import db
def home(repartidores):
    return render_template("home.html",repartidores=repartidores)