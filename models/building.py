import db


class Building(db.Model):

    def __init__(self, building_id, location):
        self.building_id = building_id
        self.location = location