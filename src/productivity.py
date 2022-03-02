from typing import List


class ProductivitySystem:
    def track_productivity(self, employees: List, hours: int):
        print('Tracking employee productivity')
        print('-' * 10)
        for employee in employees:
            employee.work(hours)
            print('')
