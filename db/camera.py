# database imports
from db.table import DatabaseTable


class CameraDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize CameraDatabaseMixin without self.db defined')

        db = getattr(self, 'db')
        self.cameras = DatabaseTable(db, 'cameras', 'c')

    def put_camera(self, camera):
        return self.cameras.set(camera, key=camera.camera_id)

    def get_camera(self, camera_id):
        return self.cameras.get(camera_id)

    def update_camera(self, camera, old_key=None):
        old_deleted = False
        if old_key:
            old_deleted = self.delete_camera(old_key)

        updated = self.cameras.set(camera, key=camera.camera_id)
        return updated and old_deleted

    def delete_camera(self, camera_id):
        return self.cameras.delete(camera_id)

    def dump_cameras(self):
        """
        Useful for debugging.
        """
        return self.cameras.dump()