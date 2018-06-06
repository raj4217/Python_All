class empl:
    def __init__(self,fname,lname,comp='HCL'):
        self.fname = fname
        self.lname = lname
        self.comp = comp
        # self.email = '{}-{}@{}.com'.format(self.fname.lower(),self.lname.lower(),self.comp.lower())

    @property
    def fullName(self):
        return self.fname+' '+self.lname

    @property
    def email(self,comp='HCL'):
        self.comp = comp
        return '{}-{}@{}.com'.format(self.fname.lower(),self.lname.lower(),self.comp.lower())

    @fullName.setter
    def fullName(self,name):
        self.fname,self.lname = name.split(' ')

    @fullName.deleter
    def fullName(self):
        self.fname = None
        self.lname = None

emp1 = empl('Raj','Sen')
emp2 = empl('Test','User')

# emp1.fullName = 'Jim Parsons'

# del empl.fullName
print(emp1.fname)
print(emp1.email)
print(emp1.fullName)

