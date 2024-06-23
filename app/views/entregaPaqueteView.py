from flask import render_template
def entregaPaqueteView(id):
    return render_template("registrarEntrega.html",id=id)