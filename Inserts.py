import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute ("INSERT INTO  EMPLOYEES VALUES (10, 'FAITH',23,13000.00)")
conn.execute ("INSERT INTO  EMPLOYEES VALUES (20, 'REAGAN',23,13000.00)")
conn.execute ("INSERT INTO  EMPLOYEES VALUES (30, 'MADOLA',23,13000.00)")
conn.execute ("INSERT INTO  EMPLOYEES VALUES (40, 'MRENA',23,13000.00)")`
conn.execute ("INSERT INTO  EMPLOYEES VALUES (50, 'ESTHER',23,13000.00)")

conn.commit()
print("Record inserted successfully")
conn.close()