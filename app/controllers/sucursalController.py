import random
from ..models.sucuarsal import Sucursal
from ..models.paquete import Paquete
from ..views.sucursalView import sucursales
from ..views.sucursalView import sucursal
from flask import  flash, redirect, render_template, request, url_for
from app import db

def sucursalController():
    try:
        list=Sucursal.query.all()
        return sucursales(list)
    except Exception as e:
        flash(str(e), 'error')
        return redirect(url_for('index'))

def sucursalNumController(id):
    try:
        sucu= Sucursal.query.get(id)
        if not sucu:
                raise ValueError(f"Sucursal con ID {id} no encontrada")
        return sucursal(sucu)
    except Exception as e:
        flash(str(e), 'error')
        return redirect(url_for('index'))
    
def createPaquete(id):
    try:
        sucu = Sucursal.query.get_or_404(id)
        numEnvio = random.randint(1000, 5000)
        if request.method == 'POST':
            nuevoPaquete = Paquete(
                numeroEnvio=numEnvio,
                peso=request.form['peso'],
                nomDestinatario=request.form['nombre'],
                dirDestinatario=request.form['direc'],
                entregado=False,
                idsucursal=id,
                idrepartidor=0,
                idtransporte=0
            )
            db.session.add(nuevoPaquete)
            db.session.commit()
            flash('Paquete registrado correctamente', 'success')
            return redirect(url_for('sucursalNum', id=id))
        return render_template('sucursalNum.html', sucursal=sucu)
    except Exception as e:
        db.session.rollback()
        flash(str(e), 'error')
        return redirect(url_for('sucursalNum', id=id))
            