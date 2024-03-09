from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from sqlalchemy.exc import OperationalError
from time import sleep
from sqlalchemy import text
from models.GrupoVotacion import GrupoVotacion
from models.LocalVotacion import LocalVotacion
from models.Departamento import Departamento
from models.Provincia import Provincia
from models.Distrito import Distrito

api=Flask(__name__)
cors=CORS(api)
api.config['SQLALCHEMY_DATABASE_URI']='mysql://u584908256_onpe:Senati2023%40@srv1101.hstgr.io/u584908256_onpe'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api.config['SQLALCHEMY_POOL_RECYCLE'] = 280
db.init_app(api)


@api.route('/')
def index():
    return render_template('index.html')

@api.route('/actas/<tipo>')
def getActasTipo(tipo):
    if tipo=='actasUbigeo':
        return render_template('actas_ubigeo.html')
    if tipo=='actasNumero':
        return render_template('actas_numero.html')
    

@api.route('/actas/<tipo>/<busqueda>')
def getActas(tipo, busqueda):
    if tipo=='actasUbigeo':
        return render_template('actas_ubigeo.html', busqueda=busqueda)
    if tipo=='actasNumero':
        print(busqueda)
        actaNumeroEncontrada=GrupoVotacion.query.filter_by(idGrupoVotacion=busqueda).first()
        if actaNumeroEncontrada==None:
            return render_template('no_encontrado.html')
        local=LocalVotacion.query.filter_by(idLocalVotacion=actaNumeroEncontrada.idLocalVotacion).first()
        distrito=Distrito.query.filter_by(idDistrito=local.idDistrito).first()
        provincia=Provincia.query.filter_by(idProvincia=distrito.idProvincia).first()
        departamento=Departamento.query.filter_by(idDepartamento=provincia.idDepartamento).first()
        return render_template('actas_numero_resultados.html', actaNumeroEncontrada=actaNumeroEncontrada, local=local, distrito=distrito, provincia=provincia, departamento=departamento)

if __name__=='__main__':
    api.run(debug=True)