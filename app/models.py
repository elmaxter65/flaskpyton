#de app se importa db
from app import db

#Se crea la tabla User que hereda de db.Model
class User(db.Model):
    #Se crea la columna id como clave primaria e integer
    id = db.Column(db.Integer, primary_key=True)
    #Se crea la columna nickname como string de tamagn 64, como unico.
    usuario = db.Column(db.String(64), index=True, unique=True)
    #Columna correo, de 120 de tamagno del string y unico.
    correo = db.Column(db.String(120), index=True, unique=True)
    #Posts. que tiene relacion con la clase Post (tabla post),
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.usuario)

#Tabla Post que hereda de model
class Post(db.Model):
    #Se crea el id del post como entero y clave primaria
    id = db.Column(db.Integer, primary_key=True)
    #Se crea la columna body como string de 140 caracteres
    cuerpo = db.Column(db.String(140))
    #Se define la marca de tiempo.
    timestamp = db.Column(db.DateTime)
    #Se define el id del usuario, es una clave foranea de la tabla usuario
    #Columna id.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.cuerpo)
