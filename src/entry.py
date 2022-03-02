import employee
import hr
import productivity


manager = employee.Manager(1, "Elghazi Ilyass", 4000)
secretary = employee.Secretary(1, "Elghazi Ilyass", 4000)
sales_person = employee.SalesPerson(2, "Zakaria", 400, 50)
factory_worker = employee.FactoryWorker(3, "Salma", 4000, 1000)
temporary_secretary = employee.TemporarySecretary(4, "Jane", 600, 40)

employees = [
    manager,
    secretary,
    sales_person,
    factory_worker,
    temporary_secretary
]
productivity_system = productivity.ProductivitySystem()
payroll_system = hr.PayrollSystem()

productivity_system.track_productivity(employees,40)
payroll_system.calculate_payroll(employees)
