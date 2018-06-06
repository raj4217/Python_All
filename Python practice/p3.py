
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay,emps=None):
        super().__init__(first,last,pay)
        if emps==None:self.emps=[]
        else:self.emps=emps

    def add_emp(self,emp):
        if emp not in self.emps:self.emps.append(emp)

    def rem_emp(self,emp):
        if emp in self.emps:self.emps.remove(emp)

    def print_emp(self):
        for emp in self.emps:
            print('-->',emp.fullname())



dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000,'Java')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.rem_emp(dev_1)
# mgr_1.print_emp()
# print(isinstance(mgr_1,Developer))
# print(issubclass(Developer,Manager))

# print(help(Developer))
# print(dev_1.email,dev_1.prog_lang)
# print(dev_2.email,dev_2.prog_lang)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
