import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute("UPDATE EMPLOYEES SET AGE = 30 WHERE ID=20")
conn.commit()
cursor= conn.execute("SELECT ID , NAME , AGE , SALARY FROM EMPLOYEES")
for row in cursor:
    print("ID", row[0])
    print("Name", row[1])
    print("Age", row[2])
    print("SALARY", row[3])

print("Records found")
conn.close()