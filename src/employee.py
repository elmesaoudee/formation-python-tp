from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


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


class Manager(SalaryEmployee):
    def work(self, hours: int):
        print("{name} is the manager and they work {hours} hours".format(
            name=self.name,
            hours=hours
        ))


class Secretary(SalaryEmployee):
    def work(self, hours: int):
        print("{name} is the secretary and they work {hours} hours".format(
            name=self.name,
            hours=hours
        ))


class SalesPerson(CommissionEmployee):
    def work(self, hours: int):
        print("{name} is the salesperson and they work {hours} hours".format(
            name=self.name,
            hours=hours
        ))


class FactoryWorker(HourlyEmployee):
    def work(self, hours: int):
        print("{name} is the factory worker and they work {hours} hours".format(
            name=self.name,
            hours=hours
        ))


class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id: int, name: str, hourly_wage: float, hours_worked: int):
        HourlyEmployee.__init__(self, id, name, hourly_wage, hours_worked)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)