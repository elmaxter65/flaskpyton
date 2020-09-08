#!/usr/bin/env python

#de migrate.versioning se importa api
from migrate.versioning import api
#De config se importa el uri
from config import SQLALCHEMY_DATABASE_URI
#De config se importa el repo de migrate
from config import SQLALCHEMY_MIGRATE_REPO
#De app se importa db
from app import db

#Se importa os.path
import os.path
#Se crea la base de datos.
db.create_all()
#Si el directorio del migrate no existe se crea y se usa,
#Si no se usa. 
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                        api.version(SQLALCHEMY_MIGRATE_REPO))
