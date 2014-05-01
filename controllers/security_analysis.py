# application imports
from db import get_database_support
from controllers import BaseController
from personnel import PersonnelController
from building_security import BuildingSecurityController
from models.log_entry import BadgeReaderLogEntry
from models.log_entry import EmployeeLogEntry
from models.log_entry import VisitorLogEntry


class SecurityAnalysisController(BaseController):

    def __init__(self, *args, **kwargs):
        super(SecurityAnalysisController, self).__init__()
        self.db = get_database_support()

    def employee_entry(self, entry_id, badge_id, time, location, result):
        log_entry = EmployeeLogEntry(entry_id=entry_id, badge_id=badge_id, name=PersonnelController().get_employee(badge_id).name, time=time, location=location, result=result)
        return self.db.put_employee_log_entry(log_entry)

    def get_employee_log_entry_debug(self):
        return self.db.dump_employee_log_entries()

    def visitor_entry(self, entry_id, badge_id, time, location, result):
        visitor = PersonnelController().get_visitor(badge_id)
        log_entry = VisitorLogEntry(entry_id=entry_id, badge_id=badge_id, name=visitor.name, associated_employee = visitor.associated_employee, time=time, location=location, result=result)
        return self.db.put_visitor_log_entry(log_entry)

    def get_visitor_log_entry_debug(self):
        return self.db.dump_visitor_log_entries()

    def badge_reader_entry(self, entry_id, badge_reader_id, badge_id, time, result):
        reader=BuildingSecurityController().get_badge_reader(badge_reader_id)
        door=BuildingSecurityController().get_door(reader.door_id)
        log_entry = BadgeReaderLogEntry(entry_id=entry_id, badge_reader_id=badge_reader_id, door_id=reader.door_id, 
                                        location=door.location, badge_id=badge_id, time=time, result=result)
        return self.db.put_badge_reader_log_entry(log_entry)

    def get_badge_reader_log_entry_debug(self):
        return self.db.dump_badge_reader_log_entries()

    def search_entry(self, badge_id, time):
        return self.db.search_entry(badge_id=badge_id, time=time)

    def employee_report(self):
        entries = self.db.get_all_employee_entries()

        report = '\n\n'
        report += '   ID    \t|   Badge\t|     Name\t|   Time\t\t| Location\t|   Result\n'
        report += '--------------------------------------------------------------------\n'
        for entry in entries:
            report += '   %s  \t|    %s\t|      %s\t|   %s\t|     %s\t|   %s\n' % (entry.entry_id, entry.badge_id, entry.name, entry.time, entry.location, entry.result)

        return report

    def visitor_report(self):
        entries = self.db.get_all_visitor_entries()

        report = '\n\n'
        report += '   ID    \t|   Badge\t|     Name\t|     Associated Employee\t|   Time\t\t| Location\t|   Result\n'
        report += '--------------------------------------------------------------------\n'
        for entry in entries:
            report += '   %s  \t|   %s\t|   %s\t|      %s\t|       %s\t|     %s\t|   %s\n' % (entry.entry_id, entry.badge_id, entry.name,
                                                               entry.associated_employee, entry.time, entry.location, entry.result)

        return report

    def badge_reader_report(self):
        entries = self.db.get_all_badge_reader_entries()

        report = '\n\n'
        report += '   ID     |  Reader  |  Door  |  Location  |  Badge  |  Time        |  Result\n'
        report += '------------------------------------------------------------------------------------\n'
        for entry in entries:
            report += '   %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s\n' % (entry.entry_id,
                                                                         entry.badge_reader_id,
                                                                         entry.door_id,
                                                                         entry.location,
                                                                         entry.badge_id,
                                                                         entry.time,
                                                                         entry.result)

        return report