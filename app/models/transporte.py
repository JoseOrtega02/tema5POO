from datetime import datetime
from . import db


class Transporte(db.Model):
    __numeroTransporte:int
    __fechaHoraLlegada:datetime
    __fechaHoraSalida:datetime
    __paquetes:object
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    _numeroTransporte = db.Column(db.Integer, unique=True, nullable=False)
    _fechaHoraSalida = db.Column(db.DateTime, nullable=False)
    _fechaHoraLlegada = db.Column(db.DateTime, nullable=False)

    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    sucursal = db.relationship('Sucursal', back_populates='transportes')

    paquetes = db.relationship('Paquete', back_populates='transporte')

    def __init__(self, numeroTransporte, fechaHoraSalida, fechaHoraLlegada, sucursal_id):
        self._numeroTransporte = numeroTransporte
        self._fechaHoraSalida = fechaHoraSalida
        self._fechaHoraLlegada = fechaHoraLlegada
        self.sucursal_id = sucursal_id

    def get_numeroTransporte(self):
        return self.__numeroTransporte

    def set_numeroTransporte(self, numeroTransporte):
        self.__numeroTransporte = numeroTransporte

    def get_fechaHoraSalida(self):
        return self.__fechaHoraSalida

    def set_fechaHoraSalida(self, fechaHoraSalida):
        self.__fechaHoraSalida = fechaHoraSalida

    def get_fechaHoraLlegada(self):
        return self.__fechaHoraLlegada

    def set_fechaHoraLlegada(self, fechaHoraLlegada):
        self.__fechaHoraLlegada = fechaHoraLlegada

    def get_paquetes(self):
        return self.__paquetes

    def set_paquetes(self, paquetes):
        self.__paquetes = paquetes

    def __repr__(self):
        return f'<Transporte {self.__numeroTransporte}>'
