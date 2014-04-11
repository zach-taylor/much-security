# database imports
from db.table import DatabaseTable


class BadgeReaderDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize BadgeReaderDatabaseMixin without self.db defined')

        db = getattr(self, 'db')
        self.badgeReaders = DatabaseTable(db, 'badgeReaders', 'br')

    def put_badgeReader(self, badgeReader):
        return self.badgeReaders.set(badgeReader, key=badgeReader.badgeReader_id)

    def get_badgeReader(self, badgeReader_id):
        return self.badgeReaders.get(badgeReader_id)

    def update_badgeReader(self, badgeReader, old_key=None):
        old_deleted = False
        if old_key:
            old_deleted = self.delete_badgeReader(old_key)

        updated = self.badgeReaders.set(badgeReader, key=badgeReader.badgeReader_id)
        return updated and old_deleted

    def delete_badgeReader(self, badgeReader_id):
        return self.badgeReaders.delete(badgeReader_id)

    def dump_badgeReaders(self):
        """
        Useful for debugging.
        """
        return self.badgeReaders.dump()