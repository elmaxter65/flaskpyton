#!/usr/bin/env python
#Se importa imp.
import imp
#Se importa api.
from migrate.versioning import api
#Se importa db de app.
from app import db
#Se importa de config uri y el repo.
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
#Se define la version de la base de datos del repo y el uri.
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se define la migracion.
migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
#Se define el modulo temporal. tomando el viejo modelo.
tmp_module = imp.new_module('old_model')
#Se crea el viejo modelo.
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se ejecuta el viejo modelo, con el temporal.
exec(old_model, tmp_module.__dict__)
#Se define el script para el modelo tomando el uri, el repo y los metadatos.
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                                          SQLALCHEMY_MIGRATE_REPO,
                                          tmp_module.meta, db.metadata)
#Se abre migration y se escribe en script.
open(migration, "wt").write(script)
#Se actualiza la base de datos a partir del uri y migrate.
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se define la version.
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se muestra en pantalla los mensajes de la nueva migracion y la version actual.
print('New migration saved as ' + migration)
print('Current database version: ' + str(v))
