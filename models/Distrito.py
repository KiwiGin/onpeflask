from utils.db import db

class Distrito(db.Model):
    __tablename__ = 'Distrito'
    
    idDistrito = db.Column(db.Integer, primary_key=True)
    idProvincia = db.Column(db.Integer)
    Detalle = db.Column(db.String(50))

