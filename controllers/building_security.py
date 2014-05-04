# application imports
from db import get_database_support
from controllers import BaseController
from models.badge_reader import BadgeReader
from models.camera import Camera
from models.door import Door


class BuildingSecurityController(BaseController):

    def __init__(self, *args, **kwargs):
        super(BuildingSecurityController, self).__init__()
        self.db = get_database_support()

    def create_badge_reader(self, door_id, badge_reader_id):
        badge_reader = BadgeReader(door_id=door_id, badge_reader_id=badge_reader_id)
        return self.db.put_badge_reader(badge_reader)

    def get_badge_reader(self, badge_reader_id):
        badge_reader_data = self.db.get_badge_reader(badge_reader_id)
        if not badge_reader_data:
            return None
        return BadgeReader(**badge_reader_data)

    def update_badge_reader(self, old_badge_reader_id, new_badge_reader_id, door_id):
        badge_reader = self.get_badge_reader(old_badge_reader_id)
        if not badge_reader:
            return False

        if new_badge_reader_id:
            badge_reader.badge_reader_id = new_badge_reader_id
        if door_id:
            badge_reader.door_id = door_id
        return self.db.update_badge_reader(badge_reader, old_key=old_badge_reader_id)

    def delete_badge_reader(self, badge_reader_id):
        return self.db.delete_badge_reader(badge_reader_id)

    def get_badge_reader_debug(self):
        return self.db.dump_badge_readers()
    
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
        return self.db.dump_cameras()
    
    def create_door(self, location, door_id, locked):
        door = Door(location=location, door_id=door_id, locked=locked)
        return self.db.put_door(door)

    def get_door(self, door_id):
        door_data = self.db.get_door(door_id)
        if not door_data:
            return None
        return Door(**door_data)

    def update_door(self, old_door_id, new_door_id, location, locked):
        door = self.get_door(old_door_id)
        if not door:
            return False

        if new_door_id:
            door.door_id = new_door_id
        if location:
            door.location = location
        if locked:
            door.locked = locked
        return self.db.update_door(door, old_key=old_door_id)

    def delete_door(self, door_id):
        return self.db.delete_door(door_id)

    def get_door_debug(self):
        return self.db.dump_doors()