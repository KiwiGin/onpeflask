from utils.db import db

class LocalVotacion(db.Model):
    __tablename__ = 'LocalVotacion'
    
    idLocalVotacion = db.Column(db.Integer, primary_key=True)
    idDistrito = db.Column(db.Integer)
    RazonSocial = db.Column(db.String(100))
    Direccion = db.Column(db.String(200))