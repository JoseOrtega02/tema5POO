from flask import render_template
def sucursales(sucursales):
    return render_template("sucursal.html",sucursales=sucursales)
def sucursal(sucursal):
    return render_template("sucursalNum.html",sucursal=sucursal)