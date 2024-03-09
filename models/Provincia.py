from utils.db import db

class Provincia(db.Model):
    __tablename__ = 'Provincia'
    
    idProvincia = db.Column(db.Integer, primary_key=True)
    idDepartamento = db.Column(db.Integer)
    Detalle = db.Column(db.String(30))