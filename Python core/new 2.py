'''
when we do print(1+2) or print('a'+'b'), it actually uses dunder add method (__add__)
i.e, print(int.__add__(1+2)) or print(str.__add__('a'+'b'))
'''


class empl:

    noOfEmp = 0
    hike = 1.04
    # comp = 'HCL'

    def __init__(self,fname,lname,pay,comp = 'HCL'):
        self.fname = fname
        self.lname = lname
        self.comp = comp
        self.email = '{}-{}@{}.com'.format(self.fname.lower(),self.lname.lower(),self.comp.lower())
        self.pay = pay
        empl.noOfEmp += 1

    def fullName(self):
        return self.fname+' '+self.lname

    def applyRaise(self):
        self.pay = int(self.pay*self.hike)

    def __repr__(self):
        return "empl('{}','{}','{}')".format(self.fname,self.lname,self.pay)

    def __str__(self):
        return self.fullName(),self.email

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())


emp1 = empl('Raj','Sen',20000)
emp2 = empl('Test','User',30000)

# print(len(emp1))
# print(emp1 + emp2)

# print(emp1)

