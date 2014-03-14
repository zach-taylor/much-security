# system imports
from os import path

# python imports
import dbm

# database imports
from db.building import BuildingDatabaseMixin
from db.employee import EmployeeDatabaseMixin
from db.visitor import VisitorDatabaseMixin


class DatabaseSupport(BuildingDatabaseMixin, EmployeeDatabaseMixin, VisitorDatabaseMixin):
    database_file = 'securitydb'

    def __init__(self):
        curdir = path.dirname(path.realpath(__file__))
        self.db = dbm.open(path.join(curdir, self.database_file), 'c')

        # call the init's for all of our database mixins so they can setup their tables
        BuildingDatabaseMixin.__init__(self)
        EmployeeDatabaseMixin.__init__(self)
        VisitorDatabaseMixin.__init__(self)