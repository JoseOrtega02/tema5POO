from flask import render_template
def transporteLlegadaView(transportes):
    return render_template("llegadaTransporte.html",transportes=transportes)