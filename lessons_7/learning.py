import sqlite3

conn = sqlite3.connect('identifier.sqlite')
cursor = conn.cursor()

cursor.execute(f"""
select *
from employee
where salary > ?
""", [2000])
for data in cursor:
    print(data)

conn.close()
