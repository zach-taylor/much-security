# application imports
from db import get_database_support
from controllers import BaseController
from models.building import Building


class BuildingController(BaseController):

    def __init__(self):
        super(BuildingController, self).__init__()
        self.db = get_database_support()

    def create_building(self, location):
        building = Building(location=location)
        return self.db.put_building(building)

    def get_building(self, location):
        building_data = self.db.get_building(location)
        if not building_data:
            return None
        return Building(**building_data)

    def update_building(self, old_location, new_location):
        building = self.get_building(old_location)
        if not building:
            return False

        if new_location:
            building.location = new_location
        return self.db.update_building(building, old_key=old_location)

    def delete_building(self, location):
        return self.db.delete_building(location)

    def lockdown_building(self, location):
        building = self.get_building(location)
        if not building:
            return False

        doors = self.db.get_all_doors(building.location)
        for d in doors:
            d.locked = 'True'
            self.db.update_door(d)
        return True

    def fire_alarm_building(self, location):
        building = self.get_building(location)
        if not building:
            return False

        doors = self.db.get_all_doors(building.location)
        for d in doors:
            d.locked = 'False'
            self.db.update_door(d)
        return True

    def get_building_debug(self):
        return self.db.dump_buildings()