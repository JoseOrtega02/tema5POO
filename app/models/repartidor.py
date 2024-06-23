from app import db

class Repartidor(db.Model):
    __numero: int
    __nombre: str
    __dni: str
    __paquetes: object
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    _numero = db.Column(db.Integer, unique=True, nullable=False)
    _nombre = db.Column(db.String(100), nullable=False)
    _dni = db.Column(db.String(20), nullable=False, unique=True)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)

    sucursal = db.relationship('Sucursal', back_populates='repartidores')
    paquetes = db.relationship('Paquete', back_populates='repartidor')

    def __init__(self, numero, nombre, dni, sucursal_id):
        self._numero = numero
        self._nombre = nombre
        self._dni = dni
        self.sucursal_id = sucursal_id


    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_paquetes(self):
        return self.__paquetes

    def set_paquetes(self, paquetes):
        self.__paquetes = paquetes

    def __repr__(self):
        return f'<Repartidor {self.__nombre}>'
