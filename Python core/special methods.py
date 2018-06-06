class empl:

    noOfEmp = 0
    hike = 1.04
    comp = 'HCL'

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = '{}-{}@{}.com'.format(self.fname.lower(), self.lname.lower(), self.comp.lower())
        self.pay = pay
        empl.noOfEmp += 1

    def fullName(self):
        return self.fname + ' ' + self.lname

    def applyRaise(self):
        self.pay = int(self.pay * self.hike)

    @classmethod
    def setHike(cls, amount):
        cls.hike = amount

    def __str__(self):
        return ',srjgns'

    def __repr__(self):
        return "Empl('{}','{}','{}')".format(self.fname, self.lname, self.pay)


emp1 = empl('Raj', 'Sen', 20000)
emp2 = empl('Test', 'User', 30000)

print(emp1)
