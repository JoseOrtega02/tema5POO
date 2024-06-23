from datetime import datetime
import random
from flask import request
from app.models.paquete import Paquete
from app.views.salidaTransporteView import salidaTransporteView
from ..models.transporte import Transporte
from ..views.transporteLlegadaView import transporteLlegadaView
from ..models.sucuarsal import Sucursal
from app import db
from ..views.seleccionarPaquetesView import seleccionarPaquetesView
def salidaTransporteController(idSucursal):
    listSucu= Sucursal.query.all()
    listSucuToShow= [sucu for sucu in listSucu if sucu.id != idSucursal]
    return salidaTransporteView(listSucuToShow)
def seleccionarPaquetesController(idsucursal):
    num = random.randint(1,40)
    if request.method == "POST":
        paquetesIds= request.form.getlist('paquetes')
        transporte= Transporte(numeroTransporte=num,fechaHoraSalida=datetime.now(),idsucursal=idsucursal)
        db.session.add(transporte)
        db.session.flush()
        for paqueteid in paquetesIds:
            paquete = Paquete.query.get(paqueteid)
            paquete.idtransporte = transporte.id
            db.session.add(paquete)
        db.session.commit()
    paquetes = Paquete.query.filter_by(entregado=False,idrepartidor=0,idtransporte=0).all()
    return seleccionarPaquetesView(paquetes)
def llegadaTransporteConreoller(idsucursal):
    if request.method == "POST":
       transid = request.form.get("transportes") 
       transporte = Transporte.query.get(transid)
       transporte.fechaHoraLlegada = datetime.now()
       db.session.add(transporte)
       db.session.commit()
    transportes = Transporte.query.filter_by(fechaHoraLlegada=None,idsucursal=idsucursal)
    return transporteLlegadaView(transportes)