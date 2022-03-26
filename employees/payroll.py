from dictionaryMixin import AsDictionaryMixin

class PayrollSystem(AsDictionaryMixin):
    def __init__(self):
        self.employee_policies = {
            1: SalaryPolicy(30000),
            2: SalaryPolicy(50000),
            3: CommissionPolicy(50000, 75000),
            4: HourlyPolicy(500),
            5: HourlyPolicy(1900)
        }

    def get_policy(self, employee_id):
        policy = self.employee_policies.get(employee_id)
        if not policy:
            return ValueError(employee_id)
        return policy

    def calculate_payroll(self, employees):
        print('___Calculating Payroll___')
        for employee in employees:
            print(employee.id, employee.name, end=', ')
            print(employee.calculate_payroll())
            if employee.address:
                print(employee.address)


class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission