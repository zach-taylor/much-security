# system imports
from os import path

# python imports
import dbm

# database imports
from db.building import BuildingDatabaseMixin
from db.employee import EmployeeDatabaseMixin
from db.visitor import VisitorDatabaseMixin
from db.badgeReader import BadgeReaderDatabaseMixin
from db.camera import CameraDatabaseMixin
from db.door import DoorDatabaseMixin


class DatabaseSupport(BuildingDatabaseMixin, EmployeeDatabaseMixin, VisitorDatabaseMixin,
                      BadgeReaderDatabaseMixin, CameraDatabaseMixin, DoorDatabaseMixin):
    database_file = 'securitydb'

    def __init__(self):
        curdir = path.dirname(path.realpath(__file__))
        self.db = dbm.open(path.join(curdir, self.database_file), 'c')

        # call the init's for all of our database mixins so they can setup their tables
        BuildingDatabaseMixin.__init__(self)
        EmployeeDatabaseMixin.__init__(self)
        VisitorDatabaseMixin.__init__(self)
        BadgeReaderDatabaseMixin.__init__(self)
        CameraDatabaseMixin.__init__(self)
        DoorDatabaseMixin.__init__(self)