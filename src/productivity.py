class EmployeeExhaustedException(Exception):
    pass


class ProductivitySystem:
    @staticmethod
    def track_productivity(employees, hours):
        return "\n".join([
            f'Tracking employee productivity',
            f'------------------------------',
            '\n'.join([f'{employee.name} : {employee.work(hours)}' for employee in employees])]
        )


class ManagerRole:
    def work(self, hours):
        if hours > 100:
            raise EmployeeExhaustedException()
        return 'Top of the food chain, and works for {hours} hours'.format(
            hours=hours
        )


class SecretaryRole:
    def work(self, hours):
        if hours > 100:
            raise EmployeeExhaustedException()
        return 'Does paper work and, works for {hours} hours'.format(
            hours=hours
        )


class SalesPersonRole:
    def work(self, hours):
        if hours > 100:
            raise EmployeeExhaustedException()
        return 'Gets phone calls and, works for {hours} hours'.format(
            hours=hours
        )


class FactoryWorkerRole:
    def work(self, hours):
        if hours > 100:
            raise EmployeeExhaustedException()
        return 'Bottom of the food chain, and works for {hours} hours'.format(
            hours=hours
        )
