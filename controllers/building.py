# application imports
from db import get_database_support
from controllers import BaseController
from models.building import Building


class BuildingController(BaseController):

    def __init__(self, *args, **kwargs):
        super(BuildingController, self).__init__(*args, **kwargs)
        self.db = get_database_support()

    def create_building(self, building_id, location):
        building = Building(building_id, location)
        return self.db.put_building(building)

    def get_building(self, building_id):
        return self.db.get_building(building_id)

    def update_building(self, building_id, location):
        building = self.get_building(building_id)
        if location:
            building.location = location
        return self.db.update_building(building)

    def delete_building(self, building_id):
        return self.db.delete_building(building_id)