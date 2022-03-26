class ProductivitySystem:

    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()

    def track(self, employees, hours):
        print('___Tracking Employee Productivity___')
        for employee in employees:
            employee.work(hours)
        print()


class ManagerRole:
    def perform_duties(self, hours):
        return 'руководил в течение', hours, 'часов'


class SecretaryRole:
    def perform_duties(self, hours):
        return 'потратил', hours, 'часов на работу с документами'


class SalesRole:
    def perform_duties(self, hours):
        return 'продавал', hours, 'часов'


class FactoryRole:
    def perform_duties(self, hours):
        return 'вел производственные работы в течение', hours, 'часов'