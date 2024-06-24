from flask import flash, redirect, request, url_for

from app.models.paquete import Paquete
from app.models.repartidor import Repartidor

from app import db
from app.views.asignarPaquetesView import asignarPaquetesView

def asignarPaqueteController(idsucursal):
    if request.method == "POST":
        try:
            repartidorId = request.form.get("repartidor")   
            paquetesIds = request.form.getlist("paquetes")
            for paqId in paquetesIds:
                paquete= Paquete.query.get(paqId)
                if not paquete:
                    raise ValueError(f"Paquete con ID {paqId} no encontrado")
                
                paquete.idrepartidor = repartidorId
                db.session.add(paquete)
                db.session.commit()
            flash('Paquetes asignados correctamente', 'success')
        except Exception as e:
            db.session.rollback()
            flash(str(e), 'error')
            return redirect(url_for('asignarPaquete', idsucursal=idsucursal))
    
    repartidores = Repartidor.query.filter_by(idsucursal=idsucursal)
    paquetes= Paquete.query.filter_by(entregado=False,idrepartidor=0)
    return asignarPaquetesView(paquetes,repartidores)