class tax:
    def __init__(self, salary, months, tax = 100):
        self.salary = salary
        self.months = months
        self.tax = tax

    def profit(self):
        return (self.salary * self.months) - self.tax

net_profit = tax(100,3)
actual_profit = net_profit.profit()

print (actual_profit)
