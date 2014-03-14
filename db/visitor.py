# database imports
from db.table import DatabaseTable


class VisitorDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize VisitorDatabaseMixin without self.db defined')

        db = getattr(self, 'db')
        self.visitors = DatabaseTable(db, 'visitors', 'e')

    def put_visitor(self, visitor):
        return self.visitors.set(visitor, key=visitor.badge_id)

    def get_visitor(self, badge_id):
        return self.visitors.get(badge_id)

    def update_visitor(self, visitor, old_key=None):
        old_deleted = False
        if old_key:
            old_deleted = self.delete_visitor(old_key)
            
        updated = self.visitors.set(visitor, key=visitor.badge_id)
        return updated and old_deleted

    def delete_visitor(self, badge_id):
        return self.visitors.delete(badge_id)

    def dump_visitors(self):
        """
        Useful for debugging.
        """
        return self.visitors.dump()