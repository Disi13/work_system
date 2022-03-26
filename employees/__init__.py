from employees.employee import *

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees

manager = employees[0]
manager.payroll = HourlyPolicy(300)

productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)

print(manager.to_dict())