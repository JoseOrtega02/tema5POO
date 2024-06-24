from datetime import datetime
import random
from flask import flash, redirect, request, url_for
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
    try:
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
            flash("REgistro Exitoso",'success')
        paquetes = Paquete.query.filter_by(entregado=False,idrepartidor=0,idtransporte=0).all()
        return seleccionarPaquetesView(paquetes)
    except Exception as e:
        flash(str(e),'error')
        return redirect(url_for('selecPaq',id=idsucursal))
def llegadaTransporteConreoller(idsucursal):
    try:
        if request.method == "POST":
           transid = request.form.get("transportes") 
           
           if transid == "" or transid == None:
               raise ValueError("No se encontro transporte",'error')
           transporte = Transporte.query.get(transid)
           transporte.fechaHoraLlegada = datetime.now()
           db.session.add(transporte)
           db.session.commit()
           flash('Llegada del transporte registrada con exito','success')
        transportes = Transporte.query.filter_by(fechaHoraLlegada=None,idsucursal=idsucursal)
        return transporteLlegadaView(transportes)
    except Exception as e:
        flash(str(e),'error')
        return redirect(url_for('transporteLlegada',id=idsucursal))