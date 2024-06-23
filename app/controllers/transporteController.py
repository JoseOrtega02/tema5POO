from datetime import datetime
import random
from flask import request
from app.models.paquete import Paquete
from app.views.salidaTransporteView import salidaTransporteView
from ..models.transporte import Transporte
from ..views.transporteView import transporteView
from ..models.sucuarsal import Sucursal
from app import db
from ..views.seleccionarPaquetesView import seleccionarPaquetesView
def transporteController():
    list= Transporte.query.all()
    return transporteView(list)

def salidaTransporteController(idSucursal):
    listSucu= Sucursal.query.all()
    listSucuToShow= [sucu for sucu in listSucu if sucu.id != idSucursal]
    return salidaTransporteView(listSucuToShow)
def seleccionarPaquetesController(idsucursal):
    num = random.randint(1,40)
    if request.method == "POST":
        paquetesIds= request.form.getlist('paquetes')
        transporte= Transporte(numeroTransporte=num,fechaHoraSalida=datetime.now())
        db.session.add(transporte)
        db.session.flush()
        for paqueteid in paquetesIds:
            paquete = Paquete.query.get(paqueteid)
            paquete.idtransporte = transporte.id
            db.session.add(paquete)
        db.session.commit()
    paquetes = Paquete.query.filter_by(entregado=False,idrepartidor=0,idtransporte=0).all()
    return seleccionarPaquetesView(paquetes)