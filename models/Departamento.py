from utils.db import db

class Departamento(db.Model):
    __tablename__ = 'Departamento'
    
    idDepartamento = db.Column(db.Integer, primary_key=True)
    Detalle = db.Column(db.String(30))
