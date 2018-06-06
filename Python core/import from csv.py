# import csv

# with open('test.csv', 'r') as f:
#     fread = csv.DictReader(f)
#     # [print(line['email']) for li  ne in fread]
#     with open('test1.csv', 'w') as wf:
#         fields = ['first_name', 'last_name']
#         wcsv = csv.DictWriter(wf, fieldnames=fields, delimiter='\t')
#         # [wcsv.writerow(line) for line in fread]
#         for line in fread:
#             del line['email']
#             wcsv.writerow(line)

# with open('test1.csv', 'r') as f_csv:
#     fread = csv.reader(f_csv, delimiter='\t')
#     [print(f) for f in fread]


class emp:
    def __init__(self,name):
        self.name = name

    def disp(self):
        # disp()
        print(self.name)

class b(emp):pass
class c(b):
    b.disp(self.name)


c =c('soumya')
c.disp()
