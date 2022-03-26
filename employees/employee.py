from address import *
from payroll import *
from productivity import *


class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print('Employee', self.id, self.name)
        print(duties)
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Ivan Ivanov',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'Petr Petrov',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Sidr Sidorov',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Roman Grushenkov',
                'role': 'factory'
            }
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)