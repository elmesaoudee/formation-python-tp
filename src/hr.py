from typing import List


class PayrollSystem:
    def calculate_payroll(self, employees: List):
        print('calculating payroll-')
        print('-' * 10)
        for employee in employees:
            print('payroll for : {id} - {name}.'.format(id=employee.id, name=employee.name))
            print('salary amount = {salary}.'.format(salary=employee.calculate_payroll()))
            print('')


class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id: int, name: str, weekly_salary: float):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id: int, name: str, hourly_wage: float, hours_worked: int):
        super().__init__(id, name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_wage


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id: int, name: str, weekly_salary: float, commission: float):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission



