# application imports
from db import get_database_support
from controllers import BaseController
from models.log_entry import BadgeReaderLogEntry
from models.log_entry import EmployeeLogEntry
from models.log_entry import VisitorLogEntry


class SecurityAnalysisController(BaseController):

    def __init__(self, *args, **kwargs):
        super(SecurityAnalysisController, self).__init__()
        self.db = get_database_support()

    def employee_entry(self, entry_id, badge_id, time, result):
        log_entry = EmployeeLogEntry(entry_id=entry_id, badge_id=badge_id, time=time, result=result)
        return self.db.put_employee_log_entry(log_entry)

    def get_employee_log_entry_debug(self):
        return self.db.dump_employee_log_entries()

    def visitor_entry(self, entry_id, badge_id, time, result):
        log_entry = VisitorLogEntry(entry_id=entry_id, badge_id=badge_id, time=time, result=result)
        return self.db.put_visitor_log_entry(log_entry)

    def get_visitor_log_entry_debug(self):
        return self.db.dump_visitor_log_entries()

    def badge_reader_entry(self, entry_id, badge_reader_id, badge_id, time, result):
        log_entry = BadgeReaderLogEntry(entry_id=entry_id, badge_reader_id=badge_reader_id,
                                        badge_id=badge_id, time=time, result=result)
        return self.db.put_badge_reader_log_entry(log_entry)

    def get_badge_reader_log_entry_debug(self):
        return self.db.dump_badge_reader_log_entries()

    def search_entry(self, badge_id, time):
        return self.db.search_entry(badge_id=badge_id, time=time)