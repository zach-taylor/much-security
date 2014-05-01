# database imports
from db.table import DatabaseTable


class BadgeReaderDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize BadgeReaderDatabaseMixin without self.db defined')

        db = getattr(self, 'db')
        self.badge_readers = DatabaseTable(db, 'badge_readers', 'br')

    def put_badge_reader(self, badge_reader):
        return self.badge_readers.set(badge_reader, key=badge_reader.badge_reader_id)

    def get_badge_reader(self, badge_reader_id):
        return self.badge_readers.get(badge_reader_id)

    def update_badge_reader(self, badge_reader, old_key=None):
        old_deleted = False
        if old_key:
            old_deleted = self.delete_badge_reader(old_key)

        updated = self.badge_readers.set(badge_reader, key=badge_reader.badge_reader_id)
        return updated and old_deleted

    def delete_badge_reader(self, badge_reader_id):
        return self.badge_readers.delete(badge_reader_id)

    def dump_badge_readers(self):
        """
        Useful for debugging.
        """
        return self.badge_readers.dump()