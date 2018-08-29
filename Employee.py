class Employee:
    number_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        Employee.number_of_emps += 1
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_info):
        first, last, pay = employee_info.split('-')
        return cls(first, last, pay)


emp1_info = "Andy-Small-12000"
emp2_info = "Shawn-Large-25000"
emp3_info = "Kareem-Very Large-3000"

emp1 = Employee.from_string(emp1_info)
emp2 = Employee('Andy', 'Phy', 10000)

Employee.set_raise_amount(1.003)

print(emp1.first)
print(emp1.email)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("Number of Employees in the Company: " + str(Employee.number_of_emps))
