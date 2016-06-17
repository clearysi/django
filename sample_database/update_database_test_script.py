__author__ = 'scleary'

import sqlite3

conn = sqlite3.connect('/home/scleary/Lab_database/db.sqlite3')
print "Opened database successfully"

cursor=conn.cursor()
cursor.execute("SELECT sql FROM sqlite_master WHERE name='table_sampleinformationauditlogentry';")
print(cursor.fetchall())
conn.execute(
    "INSERT INTO table_sampleinformation (d_number,date,worksheet_number,link,classification,first_check,second_check) VALUES ('D00.00005','2016-06-15',10005,'test_link','not_checked','not_checked','not_checked')")
conn.commit()
print "Records created successfully"
conn.close()