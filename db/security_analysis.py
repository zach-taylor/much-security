# python imports
from datetime import datetime
import itertools

# database imports
from db.table import DatabaseTable


class SecurityAnalysisDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize SecurityAnalysisDatabaseMixin without self.db'
                            + 'defined')

        db = getattr(self, 'db')
        self.employee_log_entries = DatabaseTable(db, 'employee_log_entries', 'ele')
        self.visitor_log_entries = DatabaseTable(db, 'visitor_log_entries', 'vle')
        self.badge_reader_log_entries = DatabaseTable(db, 'badge_reader_log_entries', 'brle')

    def put_log_entry(self, log_entry_table, log_entry):
        if not log_entry.entry_id:
            log_entry.entry_id = log_entry_table.get_next_uid()
        if not log_entry.time:
            log_entry.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        if not log_entry.result:
            log_entry.result = 'success'
        return log_entry_table.set(log_entry, key=log_entry.entry_id)

    def put_employee_log_entry(self, log_entry):
        return self.put_log_entry(self.employee_log_entries, log_entry)

    def get_all_employee_entries(self):
        return self.employee_log_entries.get_all()

    def dump_employee_log_entries(self):
        return self.employee_log_entries.dump()

    def put_visitor_log_entry(self, log_entry):
        return self.put_log_entry(self.visitor_log_entries, log_entry)

    def get_all_visitor_entries(self):
        return self.visitor_log_entries.get_all()

    def dump_visitor_log_entries(self):
        return self.visitor_log_entries.dump()

    def put_badge_reader_log_entry(self, log_entry):
        return self.put_log_entry(self.badge_reader_log_entries, log_entry)

    def get_all_badge_reader_entries(self):
        return self.badge_reader_log_entries.get_all()

    def dump_badge_reader_log_entries(self):
        return self.badge_reader_log_entries.dump()

    def search_entry(self, badge_id=None, time=None):
        # get all search entries
        entries = list(itertools.chain.from_iterable([
            self.employee_log_entries.get_all(),
            self.visitor_log_entries.get_all(),
            self.badge_reader_log_entries.get_all()
        ]))

        # find entries matching search criteria
        matches = []
        for entry in entries:
            match = True

            # filter by badge_id
            if badge_id and entry.badge_id != badge_id:
                match = False

            # filter by time
            if time and entry.time != time:
                match = False

            if match:
                matches.append(entry)

        return matches