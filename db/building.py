# database imports
from db.table import DatabaseTable


class BuildingDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize BuildingDatabaseMixin without self.db defined')

        db = getattr(self, 'db')
        self.buildings = DatabaseTable(db, 'buildings', 'b')

    def put_building(self, building):
        return self.buildings.set(building, key=building.location)

    def get_building(self, location):
        return self.buildings.get(location)

    def update_building(self, building, old_key=None):
        updated = self.buildings.set(building, key=building.location)
        old_deleted = False
        if old_key:
            old_deleted = self.delete_building(old_key)
        return updated and old_deleted

    def delete_building(self, location):
        return self.buildings.delete(location)

    def dump_buildings(self):
        """
        Useful for debugging.
        """
        return self.buildings.dump()