from typing import List


class PayrollSystem:
    def calculate_payroll(self, employees: List):
        print('calculating payroll-')
        print('-' * 10)
        for employee in employees:
            print('payroll for : {id} - {name}.'.format(id=employee.id, name=employee.name))
            print('salary amount = {salary}.'.format(salary=employee.calculate_payroll()))
            print('')
