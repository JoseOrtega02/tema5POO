from flask import render_template
def sucursales():
    sucursales= ["1","2","3"]
    return render_template("sucursal.html",sucursales=sucursales)
def sucursal(num):
    return render_template("sucursalNum.html",num=num)