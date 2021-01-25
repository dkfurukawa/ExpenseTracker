# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

from datetime import datetime
import calendar


class ExpenseTracker:
    def __init__(self, name: str = "", past_months: dict = None, month: int = 0):
        self._name = name
        self._current_month = month
        if not past_months:
            self._past_months = {1: 0,
                                 2: 0,
                                 3: 0,
                                 4: 0,
                                 5: 0,
                                 6: 0,
                                 7: 0,
                                 8: 0,
                                 9: 0,
                                 10: 0,
                                 11: 0,
                                 12: 0}
        else:
            self._past_months = past_months

    def print_total_expenditure(self):
        total = 0
        for key in self._past_months.keys():
            print(calendar.month_name[key] + ": $" + str(self._past_months[key]))
            total += self._past_months[key]
        print("\nTotal: " + str(total) + "\n")

    def add_to_month(self, month: int = 1, amount: int = 0):
        self._past_months[month] += amount


if __name__ == '__main__':
    today = datetime.today()
    current_month = today.month
    month_string = calendar.month_name[current_month]
    print(current_month, month_string)

    start_dict = {1: 100,
                  2: 200,
                  3: 300,
                  4: 400,
                  5: 500,
                  6: 600,
                  7: 700,
                  8: 800,
                  9: 900,
                  10: 1000,
                  11: 1100,
                  12: 1200}
    test = ExpenseTracker("me", start_dict)
    test.print_total_expenditure()

    test.add_to_month(current_month, 500)

    test.print_total_expenditure()
