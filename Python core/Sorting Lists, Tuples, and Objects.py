# ls = [9, 1, 3, 4, 2, 8, 5, 6, 4]
# ls = [9, 1, -3, 4, -2, 8, 5, 6, -4]
# ls.sort(reverse=True)
# print(ls)
# print(sorted(ls, key=abs))
# ---------------------------------------------------------
# tup = (9, 1, 3, 4, 2, 8, 5, 6, 4)
# stup = sorted(tup)
# print(tup)
# print(stup)
# __________________________________________________________

# dic = {'name': 'Raj', 'job': 'IT', 'age': '26'}
# print(sorted(dic))
# __________________________________________________________


class empl:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __repr__(self):
        return "Empl('{}','{}','{}')".format(self.fname, self.lname, self.pay)


from operator import attrgetter
emp1 = empl('Raj', 'Sen', 20000)
emp2 = empl('Test', 'User', 30000)
emps = [emp1, emp2]
semp = sorted(emps, key=attrgetter('pay'), reverse=True)
print(semp)
