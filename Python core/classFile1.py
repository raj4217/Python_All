class emp:
    company = 'HCL'
    hike = 1.1
    numOfEmp = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname.lower() + '.' + lname.lower() + '@' + self.company.lower() + '.com'
        self.pay = pay
        emp.numOfEmp += 1

    def fullName(self):
        return self.fname + ' ' + self.lname

    def payHike(self):
        return round(self.pay * self.hike)

    def email(self):
        return '{}.{}@hcl.com'.format(self.fname, self.lname)


emp1 = emp('Soumya', 'Sen', 25000)
emp1 = emp('Raj', 'Karmakar', 30000)
# print(emp1.__dict__)
# #
# emp1.company = 'Infy'
# print(emp1.__dict__)
# # print(emp1.fullName())
# print(emp1.email())

# # print(emp.fullName(emp1))
# # emp1.hike
# print(emp1.payHike())
print(emp.numOfEmp)
