#Se importa os
import os
#Se define el directorio base del proyecto
basedir = os.path.abspath(os.path.dirname(__file__))

#Se habilita CSRF
CSRF_ENABLED = True
#Se define la clave secreta
SECRET_KEY = 'prueba'


PROVEEDORES_OPENID = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'}]

#Se define el uri de la base de datos sqlite app.db
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#Se define el repositorio para migracion de la base de datos app.db
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
