from datetime import datetime
from app import db


class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numeroTransporte = db.Column(db.Integer, unique=True, nullable=False)
    fechaHoraSalida = db.Column(db.DateTime, nullable=False)
    fechaHoraLlegada = db.Column(db.DateTime, nullable=False)

    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='transporte', lazy=True)