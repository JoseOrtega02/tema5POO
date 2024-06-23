from flask import render_template
def transporteView(transportes):
    return render_template("transporte.html",transportes=transportes)