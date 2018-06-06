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

    @classmethod
    def setComp(cls, comp):
        cls.comp = comp

    @classmethod
    def strParse(cls, str):
        fname, lname, pay = str.split('-')
        return cls(fname, lname, pay)

    @staticmethod
    def dayChecker(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class devl(empl):
    hike = 1.10

    def __init__(self, fname, lname, pay, progLang):
        # empl.__init__(self, fname, lname, pay)
        super().__init__(fname, lname, pay)
        self.progLang = progLang


class mngr(empl):
    def __init__(self, fname, lname, pay, empls=None):
        super().__init__(fname, lname, pay)
        self.empls = [] if empls is None else empls

    def addEmp(self, empls):
        if empls not in self.empls:
            self.empls.append(empls)

    def rmvEmp(self, empls):
        if empls in self.empls:
            self.empls.remove(empls)

    def printEmpls(self):
        for e in self.empls:
            print('\t' + e.fullName())


dev1 = devl('Raj', 'Sen', 20000, 'C')
dev2 = devl('Test', 'User', 30000, 'Python')


print(issubclass(mngr, devl))

mng1 = mngr('Ragu', 'Vendra', 9000, [dev1])
# print(mng1.email)


# emp1 = devl('Raj','Sen',20000,'C')
# emp2 = devl('Test','User',30000)

# print(emp1.progLang)


# print(emp1.email)
# print(emp2.email)

# print(emp1.pay)
# emp1.applyRaise()
# print(emp1.pay)
# print(emp2.pay)
# print(help(devl))


# emp1 = empl('Raj','Sen',20000)
# # empl.setComp('Infy')
# emp2 = empl('Test','User',30000)
# #
# emp1.setHike(1.05)
# print(empl.hike)
# print(emp1.hike)
# print(emp2.hike)
# #
# # empl.setComp('Infy')


# empStr1 = 'Raj-Sen-2000'
# empStr2 = 'Test-User-5000'
#
# emp1 = empl.strParse(empStr1)
# emp2 = empl.strParse(empStr2)
#
# print(emp1.email)
# print(emp2.email)
# print(emp1.pay)
# print(emp2.pay)

#
# import datetime
# date = datetime.date(2018, 3, 4)
# print(empl.dayChecker(date))
