'''
parsing a csv file to create a table and then the reverse
'''
import sqlite3
import csv


conn = sqlite3.connect('sample.db')

crsr = conn.cursor()

crsr.execute('select * from profile')
fieldname = [f[0] for f in crsr.description]
print(fieldname)
with open('test2.csv', 'w', newline='') as csvfile:
    wfile = csv.writer(csvfile, delimiter='\t')

    wfile.writerow(fieldname)

    tblCntnt = crsr.fetchall()

    for line in tblCntnt:
        # print(line)
        # break
        wfile.writerow(line)


conn.commit()
conn.close()


# crsr.execute("""create table profile (first_name text,last_name text,email text)""")

# with open('test.csv', 'r') as fopen:
#     fread = csv.reader(fopen)
#     field = next(fread)
#     # print(field[0], field[1], field[2])

#     # crsr.execute('create table profile({} text,{} text,{} text)'.format(field[0], field[1], field[2]))

#     for a in fread:
#         stmt = "insert into profile values('{}','{}','{}')".format(a[0], a[1], a[2])
#         # crsr.execute(stmt)

# crsr.execute('select * from profile')
# print(crsr.fetchall())

# conn.commit()
# conn.close()
