from app import db

class Repartidor(db.Model):
    __tablename__='repartidor'
    id = db.Column(db.Integer,primary_key=True)
    numero = db.Column(db.Integer,nullable=False)
    nombre= db.Column(db.String(120),nullable=False)
    dni=db.Column(db.String(8),nullable=False)
    idsucursal=db.Column(db.Integer,nullable=True)