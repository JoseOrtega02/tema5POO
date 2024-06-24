from ..models.repartidor import Repartidor
from ..views.homeView import home
from flask import render_template
from app.models.repartidor import Repartidor

def homeController():
    list = Repartidor.query.all()
    return home(list)

def homeController():
    repartidores = Repartidor.query.all()
    return render_template('home.html', repartidores=repartidores)
