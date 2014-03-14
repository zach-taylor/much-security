# system imports
from os import path

# python imports
import dbm
import json


class DatabaseTable(object):

    def __init__(self, db, table_name):
        self.table_name = table_name
        self.db = db
        if table_name in db:
            self.table = json.loads(db[table_name])
        else:
            self.table = {}

    def set(self, key, entity):
        self.table[key] = entity.to_JSON()
        self.commit()
        return True

    def get(self, key):
        if key in self.table:
            return json.loads(self.table[key])
        return None

    def delete(self, key):
        if key in self.table:
            del self.table[key]
        return True

    def dump(self):
        return self.table

    def commit(self):
        self.db[self.table_name] = json.dumps(self.table)


class DatabaseSupport(object):
    database_file = 'securitydb'

    def __init__(self):
        curdir = path.dirname(path.realpath(__file__))
        self.db = dbm.open(path.join(curdir, self.database_file), 'c')
        self.buildings = DatabaseTable(self.db, 'buildings')

    def put_building(self, building):
        return self.buildings.set(building.building_id, building)

    def get_building(self, building_id):
        return self.buildings.get(building_id)

    def update_building(self, building):
        return self.buildings.set(building.building_id, building)

    def delete_building(self, building_id):
        return self.buildings.delete(building_id)

    def dump_buildings(self):
        """
        Useful for debugging.
        """
        return self.buildings.dump()


class Model(object):

    def __init__(self, **data):
        for prop, value in data.iteritems():
            setattr(self, prop, value)

    def __repr__(self):
        return self.to_JSON()

    def to_JSON(self):
        return json.dumps(self.__dict__)


# global db support instance
global_db = DatabaseSupport()


def get_database_support():
    """
    Get the global instance of the application's database support.
    """
    return global_db