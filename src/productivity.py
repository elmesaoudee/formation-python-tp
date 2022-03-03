class ProductivitySystem:
    @staticmethod
    def track_productivity(employees, hours):
        print('Tracking employee productivity')
        print('------------------------------')
        for employee in employees:
            result = employee.work(hours)
            print('{name} : {result}'.format(
                name=employee.name,
                result=result
            ))
        print('')


class ManagerRole:
    def work(self, hours):
        return 'Top of the food chain, and works for {hours} hours'.format(
            hours=hours
        )


class SecretaryRole:
    def work(self, hours):
        return 'Does paper work and, works for {hours} hours'.format(
            hours=hours
        )


class SalesPersonRole:
    def work(self, hours):
        return 'Gets phone calls and, works for {hours} hours'.format(
            hours=hours
        )


class FactoryWorkerRole:
    def work(self, hours):
        return 'Bottom of the food chain, and works for {hours} hours'.format(
            hours=hours
        )
