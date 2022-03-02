import hr

salary_employee = hr.SalaryEmployee(1, 'Elghazi Ilyass', 4000)
hourly_employee = hr.HourlyEmployee(2, 'Zakraria', 400, 50)
commission_employee = hr.CommissionEmployee(3, 'Salma', 4000, 1000)

payroll_system = hr.PayrollSystem()

payroll_system.calculate_payroll([salary_employee, hourly_employee, commission_employee])

