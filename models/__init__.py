# python imports
import json


class Model(object):

    def __init__(self, **data):
        for prop, value in data.iteritems():
            setattr(self, prop, value)

    def __repr__(self):
        return self.to_JSON()

    def to_JSON(self):
        return json.dumps(self.__dict__)