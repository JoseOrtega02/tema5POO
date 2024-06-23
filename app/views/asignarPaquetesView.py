from flask import render_template
def asignarPaquetesView(paquetes,repartidores):
    return render_template("asignarPaquetes.html",paquetes=paquetes,repartidores=repartidores)