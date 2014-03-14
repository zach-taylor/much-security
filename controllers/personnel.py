# application imports
from db import get_database_support
from controllers import BaseController
from models.employee import Employee
from models.visitor import Visitor


class PersonnelController(BaseController):

    def __init__(self, *args, **kwargs):
        super(PersonnelController, self).__init__()
        self.db = get_database_support()

    def create_employee(self, badge_id, name):
        employee = Employee(badge_id=badge_id, name=name)
        return self.db.put_employee(employee)

    def get_employee(self, badge_id):
        employee_data = self.db.get_employee(badge_id)
        if not employee_data:
            return None
        return Employee(**employee_data)

    def update_employee(self, old_badge_id, new_badge_id, name):
        employee = self.get_employee(old_badge_id)
        if not employee:
            return False

        if new_badge_id:
            employee.badge_id = new_badge_id
        if name:
            employee.name = name
        return self.db.update_employee(employee, old_key=old_badge_id)

    def delete_employee(self, badge_id):
        return self.db.delete_employee(badge_id)

    def get_employee_debug(self):
        return self.db.dump_employees()

    def create_visitor(self, badge_id, name, associated_employee):
        visitor = Visitor(badge_id=badge_id, name=name, associated_employee=associated_employee)
        return self.db.put_visitor(visitor)

    def get_visitor(self, badge_id):
        visitor_data = self.db.get_visitor(badge_id)
        if not visitor_data:
            return None
        return Visitor(**visitor_data)

    def update_visitor(self, old_badge_id, new_badge_id, name, associated_employee):
        visitor = self.get_visitor(old_badge_id)
        if not visitor:
            return False

        if new_badge_id:
            visitor.badge_id = new_badge_id
        if name:
            visitor.name = name
        if associated_employee:
            visitor.associated_employee = associated_employee
        return self.db.update_visitor(visitor, old_key=old_badge_id)

    def delete_visitor(self, badge_id):
        return self.db.delete_visitor(badge_id)

    def get_visitor_debug(self):
        return self.db.dump_visitors()