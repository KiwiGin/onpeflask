from utils.db import db

class GrupoVotacion(db.Model):
    __tablename__ = 'GrupoVotacion'
    
    idLocalVotacion = db.Column(db.Integer, primary_key=True)
    idGrupoVotacion = db.Column(db.String(6), primary_key=True)
    nCopia = db.Column(db.String(3))
    idEstadoActa= db.Column(db.Integer)
    ElectoresHabiles= db.Column(db.Integer)
    TotalVotantes= db.Column(db.Integer)
    P1= db.Column(db.Integer)
    P2= db.Column(db.Integer)
    VotosBlancos= db.Column(db.Integer)
    VotosNulos= db.Column(db.Integer)
    VotosImpugnados= db.Column(db.Integer)
