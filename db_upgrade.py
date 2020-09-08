#!/usr/bin/env python
#Se importa api.
from migrate.versioning import api
#De config se importa URI y el repo.
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
#Se actualiza el api.
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se define la version del api.
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se muestra la nueva version.
print('Current database version: ' + str(v))
