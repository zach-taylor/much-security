import db
import json

class Building(db.Model):

    def __init__(self, building_id, location):
        self.building_id = building_id
        self.location = location

    def __repr__(self):
        return self.to_JSON()
