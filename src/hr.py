class PayrollSystem:
    @staticmethod
    def calculate_payroll(employees):
        print('Calculating payroll ...')
        print('-----------------------')
        for employee in employees:
            print('Payroll for employee : {id} {name}'.format(
                id=employee.id,
                name=employee.name,
            ))

            print('- Check amount : {amount}'.format(
                amount=employee.calculate_payroll()
            ))

            print('')


class HourlyPolicy:
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.hours_worked


class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commision = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commision
