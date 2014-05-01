# lib imports
from datetime import datetime

# database imports
from db.table import DatabaseTable


class LogEntryDatabaseMixin(object):

    def put_log_entry(self, log_entry_table, log_entry):
        if not log_entry.entry_id:
            log_entry.entry_id = log_entry_table.get_next_uid()
        if not log_entry.time:
            log_entry.time = str(datetime.now())
        if not log_entry.result:
            log_entry.result = 'success'
        return log_entry_table.set(log_entry, key=log_entry.entry_id)

    def get_log_entry(self, log_entry_table, entry_id):
        return log_entry_table.get(entry_id)

    def dump_log_entries(self, log_entry_table):
        return log_entry_table.dump()


class EmployeeLogEntryDatabaseMixin(LogEntryDatabaseMixin):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize EmployeeLogEntryDatabaseMixin without self.db'
                            + 'defined')

        db = getattr(self, 'db')
        self.employee_log_entries = DatabaseTable(db, 'employee_log_entries', 'ele')

    def put_employee_log_entry(self, log_entry):
        return self.put_log_entry(self.employee_log_entries, log_entry)

    def get_employee_log_entry(self, entry_id):
        return self.get_log_entry(self.employee_log_entries, entry_id)

    def dump_employee_log_entries(self):
        return self.dump_log_entries(self.employee_log_entries)


class VisitorLogEntryDatabaseMixin(LogEntryDatabaseMixin):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize VisitorLogEntryDatabaseMixin without self.db'
                            + 'defined')

        db = getattr(self, 'db')
        self.visitor_log_entries = DatabaseTable(db, 'visitor_log_entries', 'vle')

    def put_visitor_log_entry(self, log_entry):
        return self.put_log_entry(self.visitor_log_entries, log_entry)

    def get_visitor_log_entry(self, entry_id):
        return self.get_log_entry(self.visitor_log_entries, entry_id)

    def dump_visitor_log_entries(self):
        return self.dump_log_entries(self.visitor_log_entries)


class BadgeReaderLogEntryDatabaseMixin(LogEntryDatabaseMixin):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize BadgeReaderLogEntryDatabaseMixin without self.db'
                            + 'defined')

        db = getattr(self, 'db')
        self.badge_reader_log_entries = DatabaseTable(db, 'badge_reader_log_entries', 'brle')

    def put_badge_reader_log_entry(self, log_entry):
        return self.put_log_entry(self.badge_reader_log_entries, log_entry)

    def get_badge_reader_log_entry(self, entry_id):
        return self.get_log_entry(self.badge_reader_log_entries, entry_id)

    def dump_badge_reader_log_entries(self):
        return self.dump_log_entries(self.badge_reader_log_entries)