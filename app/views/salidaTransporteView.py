from flask import render_template
def salidaTransporteView(list):
    return render_template("salidaTransporte.html",sucursales=list)