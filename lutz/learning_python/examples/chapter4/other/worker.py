class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.00 + percent)


bob = Worker('Bob Smith', 50000)
print(bob.last_name())
sue = Worker('Sue Jones', 60000)
sue.give_raise(.10)
print(sue.last_name(), sue.pay)
