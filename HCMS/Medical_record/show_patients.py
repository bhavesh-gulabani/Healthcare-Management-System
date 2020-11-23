#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn


cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
cursor.execute("select * from patient")

print('<html><head><title>Show Patients</title><link rel="stylesheet" type="text/css" href="../css/show-table.css"></head>')
print('<body><header><h1>Registered Patients</h1></header>')
print('<div class="wrapper">')
print('<table><tr><th>Patient ID</th><th>Patient Name</th><th>Sex</th><th>Date of birth</th><th>Age</th><th>E-mail ID</th><th>Address</th>')
for P_ID,Name,Sex,DOB,Age,Email,Address in cursor:
    print('<tr><td>',P_ID,'</td><td>',Name,'</td><td>',Sex,'</td><td>',DOB,'</td><td>',Age,'</td><td>',Email,'</td><td>',Address,'</td>')
print('</table>')
print('</div>')
print('<div class="tailer"><a class="back" href="./medical_record.html">Back</a></div>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
