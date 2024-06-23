from flask import render_template
def repartidorView(id):
    return render_template("repartidor.html",id=id)