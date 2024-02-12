import sqlite3
conn = sqlite3.connect('test.db')
print('Opened database successfully')

conn.execute ("DELETE FROM EMPLOYEES WHERE ID=10")
conn.commit()
cursor= conn.execute("SELECT ID , NAME , AGE , SALARY FROM EMPLOYEES")
for row in cursor:
    print("ID", row[0])
    print("Name", row[1])
    print("Age", row[2])
    print("SALARY", row[3])