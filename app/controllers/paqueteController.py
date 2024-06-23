from flask import request

from app.models.paquete import Paquete
from app.models.repartidor import Repartidor

from app import db
from app.views.asignarPaquetesView import asignarPaquetesView

def asignarPaqueteController(idsucursal):
    if request.method == "POST":
        repartidorId = request.form.get("repartidor")   
        paquetesIds = request.form.getlist("paquetes")
        for paqId in paquetesIds:
            paquete= Paquete.query.get(paqId)
            paquete.idrepartidor = repartidorId
            db.session.add(paquete)
            db.session.commit()
    repartidores = Repartidor.query.filter_by(idsucursal=idsucursal)
    paquetes= Paquete.query.filter_by(entregado=False,idrepartidor=0)
    return asignarPaquetesView(paquetes,repartidores)