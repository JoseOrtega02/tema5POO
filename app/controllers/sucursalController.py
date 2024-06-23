import random
from ..models.sucuarsal import Sucursal
from ..models.paquete import Paquete
from ..views.sucursalView import sucursales
from ..views.sucursalView import sucursal
from flask import  flash, redirect, render_template, request, url_for
from app import db
def sucursalController():
    list=Sucursal.query.all()
    return sucursales(list)
def sucursalNumController(id):
    sucu= Sucursal.query.get(id)
    
    return sucursal(sucu)
def createPaquete(id):
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
        