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
            repartidor = Repartidor.query.filter_by(dni=dni,numero=numero).first()
            if not repartidor:
                raise ValueError("Repartidor no encontrado")
            return redirect(url_for('repartidor', id=repartidor.id))
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('loginRepartidor'))
    return loginRepartidorView()

def repartidorController(idrepartidor):
    if request.method == "POST":
        numeroE = request.form.get("numero")
        paquete = Paquete.query.filter_by(numeroEnvio=numeroE,idrepartidor=idrepartidor).first()
        redirect(url_for("registrarEntrega",id=paquete.id))
        if paquete:
            # Redirigir a la vista para registrar la entrega del paquete
            return redirect(url_for("registrarEntrega", id=paquete.id))
        else:
            return "Paquete no encontrado para este repartidor", 404
    return repartidorView(idrepartidor)

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