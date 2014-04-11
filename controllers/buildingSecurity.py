# application imports
from db import get_database_support
from controllers import BaseController
from models.badgeReader import BadgeReader
from models.camera import Camera
from models.door import Door


class BuildingSecurityController(BaseController):

    def __init__(self, *args, **kwargs):
        super(BuildingSecurityController, self).__init__()
        self.db = get_database_support()

    def create_badgeReader(self, door_id, badgeReader_id):
        badgeReader = BadgeReader(door_id=door_id, badgeReader_id=badgeReader_id)
        return self.db.put_badgeReader(badgeReader)

    def get_badgeReader(self, badgeReader_id):
        badgeReader_data = self.db.get_badgeReader(badgeReader_id)
        if not badgeReader_data:
            return None
        return BadgeReader(**badgeReader_data)

    def update_badgeReader(self, old_badgeReader_id, new_badgeReader_id, door_id):
        badgeReader = self.get_badgeReader(old_badgeReader_id)
        if not badgeReader:
            return False

        if new_badgeReader_id:
            badgeReader.badgeReader_id = new_badgeReader_id
        if door_id:
            badgeReader.door_id = door_id
        return self.db.update_badgeReader(badgeReader, old_key=old_badgeReader_id)

    def delete_badgeReader(self, badgeReader_id):
        return self.db.delete_badgeReader(badgeReader_id)

    def get_badgeReader_debug(self):
        return self.db.dump_badgeReader()
    
    def create_camera(self, location, camera_id):
        camera = Camera(location=location, camera_id=camera_id)
        return self.db.put_camera(camera)

    def get_camera(self, camera_id):
        camera_data = self.db.get_camera(camera_id)
        if not camera_data:
            return None
        return Camera(**camera_data)

    def update_camera(self, old_camera_id, new_camera_id, location):
        camera = self.get_camera(old_camera_id)
        if not camera:
            return False

        if new_camera_id:
            camera.camera_id = new_camera_id
        if location:
            camera.location = location
        return self.db.update_camera(camera, old_key=old_camera_id)

    def delete_camera(self, camera_id):
        return self.db.delete_camera(camera_id)

    def get_camera_debug(self):
        return self.db.dump_camera()
    
    def create_door(self, location, door_id):
        door = Door(location=location, door_id=door_id)
        return self.db.put_door(door)

    def get_door(self, door_id):
        door_data = self.db.get_door(door_id)
        if not door_data:
            return None
        return Door(**door_data)

    def update_door(self, old_door_id, new_door_id, location):
        door = self.get_door(old_door_id)
        if not door:
            return False

        if new_door_id:
            door.door_id = new_door_id
        if location:
            door.location = location
        return self.db.update_door(door, old_key=old_door_id)

    def delete_door(self, door_id):
        return self.db.delete_door(door_id)

    def get_door_debug(self):
        return self.db.dump_door()