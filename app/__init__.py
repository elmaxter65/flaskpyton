#Se importa Flask
from flask import Flask
#Se importa SQLALchemy
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#Se crea la instancia de flask
app = Flask(__name__)
#Se define la configuracion
app.config.from_object('config')
#SE instancia la base de datos
db = SQLAlchemy(app)
#Se importa views y models de app
from app import views, models
