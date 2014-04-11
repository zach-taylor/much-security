# database imports
from db.table import DatabaseTable


class DoorDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize DoorDatabaseMixin without self.db defined')

        db = getattr(self, 'db')
        self.doors = DatabaseTable(db, 'doors', 'd')

    def put_door(self, door):
        return self.doors.set(door, key=door.door_id)

    def get_door(self, door_id):
        return self.doors.get(door_id)

    def update_door(self, door, old_key=None):
        old_deleted = False
        if old_key:
            old_deleted = self.delete_door(old_key)

        updated = self.doors.set(door, key=door.door_id)
        return updated and old_deleted

    def delete_door(self, door_id):
        return self.doors.delete(door_id)

    def dump_doors(self):
        """
        Useful for debugging.
        """
        return self.doors.dump()