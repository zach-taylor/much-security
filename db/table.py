# python imports
import json


class DatabaseTable(object):

    def __init__(self, db, table_name, id_prefix='uid'):
        self.table_name = table_name
        self.id_prefix = id_prefix
        self.db = db
        if table_name in db:
            self.table = json.loads(db[table_name])
        else:
            self.table = {}

        self.id_count = False

    def get_next_uid(self):
        # initialize id_count if necessary
        if not self.id_count:
            self.id_count = 0
            for key, entity in self.table.iteritems():
                num = int(key.replace(self.id_prefix, ''))
                if num > self.id_count:
                    self.id_count = num

        self.id_count += 1
        return '%s%s' % (self.id_prefix, self.id_count)

    def set(self, entity, key=None):
        if not key:
            key = self.get_next_uid()
        self.table[key] = entity.to_JSON()
        self.commit()
        return True

    def get(self, key):
        if key in self.table:
            return json.loads(self.table[key])
        return None

    def delete(self, key):
        if key in self.table:
            del self.table[key]
        return True

    def dump(self):
        return self.table

    def commit(self):
        self.db[self.table_name] = json.dumps(self.table)