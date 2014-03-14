# database imports
from db.table import DatabaseTable


class EmployeeDatabaseMixin(object):

    def __init__(self):
        if not hasattr(self, 'db'):
            raise Exception('Cannot initialize EmployeeDatabaseMixin without self.db defined')

        db = getattr(self, 'db')
        self.employees = DatabaseTable(db, 'employees', 'e')

    def put_employee(self, employee):
        return self.employees.set(employee, key=employee.badge_id)

    def get_employee(self, badge_id):
        return self.employees.get(badge_id)

    def update_employee(self, employee, old_key=None):
        old_deleted = False
        if old_key:
            old_deleted = self.delete_employee(old_key)

        updated = self.employees.set(employee, key=employee.badge_id)
        return updated and old_deleted

    def delete_employee(self, badge_id):
        return self.employees.delete(badge_id)

    def dump_employees(self):
        """
        Useful for debugging.
        """
        return self.employees.dump()