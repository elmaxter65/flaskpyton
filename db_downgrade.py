#!/usr/bin/env python

#se importa api.
from migrate.versioning import api
#Se importa el uri y el migrate.
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

#se define la version de la db para las migraciones.
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se baja una version.
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
#Se vuelva a definir el uri y migrate de la vesion.
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se muestra en pantalla la version actual.
print('Current database version: ' + str(v))
