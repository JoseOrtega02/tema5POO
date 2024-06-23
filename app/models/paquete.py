from . import db

class Paquete(db.Model):
    __numeroEnvio: int
    __peso: float
    __nombreDestinatario: str
    __direccionDestinatario: str
    __entregado: bool
    __observaciones: str
    __repartidor: object
    __sucursal: object
    __transporte: object

    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    _numeroEnvio = db.Column(db.Integer, unique=True, nullable=False)
    _peso = db.Column(db.Float, nullable=False)
    _nombreDestinatario = db.Column(db.String(100), nullable=False)
    _direccionDestinatario = db.Column(db.String(200), nullable=False)
    _entregado = db.Column(db.Boolean, default=False)
    _observaciones = db.Column(db.String(300))

    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    repartidor_id = db.Column(db.Integer, db.ForeignKey('repartidor.id'))
    transporte_id = db.Column(db.Integer, db.ForeignKey('transporte.id'))

    sucursal = db.relationship('Sucursal', back_populates='paquetes')
    repartidor = db.relationship('Repartidor', back_populates='paquetes')
    transporte = db.relationship('Transporte', back_populates='paquetes')

    def __init__(self, numeroEnvio, peso, nombreDestinatario, direccionDestinatario, entregado, observaciones, sucursal_id, repartidor_id=None, transporte_id=None):
        self._numeroEnvio = numeroEnvio
        self._peso = peso
        self._nombreDestinatario = nombreDestinatario
        self._direccionDestinatario = direccionDestinatario
        self._entregado = entregado
        self._observaciones = observaciones
        self.sucursal_id = sucursal_id
        self.repartidor_id = repartidor_id
        self.transporte_id = transporte_id

    def get_numeroEnvio(self):
        return self.__numeroEnvio

    def set_numeroEnvio(self, numeroEnvio):
        self.__numeroEnvio = numeroEnvio

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_nombreDestinatario(self):
        return self.__nombreDestinatario

    def set_nombreDestinatario(self, nombreDestinatario):
        self.__nombreDestinatario = nombreDestinatario

    def get_direccionDestinatario(self):
        return self.__direccionDestinatario

    def set_direccionDestinatario(self, direccionDestinatario):
        self.__direccionDestinatario = direccionDestinatario

    def get_entregado(self):
        return self.__entregado

    def set_entregado(self, entregado):
        self.__entregado = entregado

    def get_observaciones(self):
        return self.__observaciones

    def set_observaciones(self, observaciones):
        self.__observaciones = observaciones

    def get_repartidor(self):
        return self.__repartidor

    def set_repartidor(self, repartidor):
        self.__repartidor = repartidor

    def get_sucursal(self):
        return self.__sucursal

    def set_sucursal(self, sucursal):
        self.__sucursal = sucursal

    def get_transporte(self):
        return self.__transporte

    def set_transporte(self, transporte):
        self.__transporte = transporte

    def __repr__(self):
        return f'<Paquete {self.__numeroEnvio}>'