from src import hr
from src import productivity
from src import employees


manager = employees.Manager(1, 'Zakaria', 700)
secretary = employees.Secretary(1, 'Zakaria', 700)
sales_person = employees.SalesPerson(3, 'Meryem', 500, 300)
factory_worker = employees.FactoryWorker(2, 'Amine', 28, 20)
temporary_secretary = employees.TemporarySecretary(5, 'Amina', 40, 15)


emps = [
    manager,
    secretary,
    sales_person,
    factory_worker,
    temporary_secretary
]


print(productivity.ProductivitySystem.track_productivity(emps, 40))
hr.PayrollSystem.calculate_payroll(emps)
# print(''.join([f'{employee.name} : {employee.work(40)}\n' for employee in emps]))
