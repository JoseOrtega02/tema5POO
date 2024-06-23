from app import db

class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    numeroEnvio = db.Column(db.Integer, unique=True, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    nomDestinatario = db.Column(db.String(100), nullable=False)
    dirDestinatario = db.Column(db.String(200), nullable=False)
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.String(300))

    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))