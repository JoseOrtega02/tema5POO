from flask import render_template
def seleccionarPaquetesView(list):
    return render_template("seleccionarPaquetes.html",paquetes=list)