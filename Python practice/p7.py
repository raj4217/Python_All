import sqlite3

con = sqlite3.connect('sample.db')
cur = con.cursor()


# cur.execute('''alter table SALARYGRADE rename to salgrade ''')
# cur.execute('''alter table BONUS rename to bonus ''')
# cur.execute('''alter table PROJECT rename to project ''')
# cur.execute('''alter table PROJECT_PARTICIPATION rename to projpart ''')
# cur.execute('''alter table ROLE rename to role ''')
# cur.execute("SELECT * FROM sqlite_master")
# for f in cur.fetchall():
#     print(f'{f}')

# cur.execute('''select * from emp''')
# for f in cur.fetchall():
#     print(f'{f}')

con.commit()
con.close()
