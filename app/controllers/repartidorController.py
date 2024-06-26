from flask import flash, redirect, request, url_for

from app.models.paquete import Paquete
from app.models.repartidor import Repartidor
from app.views.entregaPaqueteView import entregaPaqueteView
from app.views.loginRepartidorView import loginRepartidorView
from app.views.repartidorView import repartidorView
from app import db

def loginRepartidorController():
    if request.method == "POST":
        try:
            dni = request.form.get("dni")
            numero = request.form.get("numero")
            if  not dni.isdigit() or  not numero.isdigit():
                raise TypeError("Debe de ser un numero enero")
            repartidor = Repartidor.query.filter_by(dni=dni,numero=numero).first()
            if not repartidor:
                raise ValueError("Repartidor no encontrado")
            return redirect(url_for('repartidor', id=repartidor.id))
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('log'))
    return loginRepartidorView()

def repartidorController(idrepartidor):
    try:
        if request.method == "POST":
            numeroE = request.form.get("numero")
            paquete = Paquete.query.filter_by(numeroEnvio=numeroE,idrepartidor=idrepartidor).first()
            print(paquete)
            if paquete:
                return redirect(url_for("registrarEntrega", id=paquete.id))
            else:
                raise ValueError("Paquete no encontrado para este repartidor")
        return repartidorView(idrepartidor)
    except Exception as e:
        flash(str(e),'error')
        return redirect(url_for("repartidor",id=idrepartidor))

def entregaPaqueteController(idPaquete):
    if request.method == "POST":
        estado = request.form.get("estado")
        if estado == "True":
            estado = True
        elif estado == "False":
            estado = False
        obs= request.form.get("observaciones")
        paquete = Paquete.query.get(idPaquete)
        paquete.entregado = estado
        paquete.observaciones = obs
        db.session.add(paquete)
        db.session.commit()
    return entregaPaqueteView(idPaquete)