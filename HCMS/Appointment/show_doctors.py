#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn


cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
cursor.execute("select employee.E_ID,Name,Sex,Salary,Qualification,Speciality from employee,doctor where employee.E_ID=doctor.doctor_ID")

print('<html><head><title>Show Doctors</title><link rel="stylesheet" type="text/css" href="../css/show-table.css"></head>')
print('<body><header><h1>Hospital Doctors</h1></header>')
print('<div class="wrapper">')
print('<table><tr><th>Doctor ID</th><th>Doctor Name</th><th>Sex</th><th>Salary</th><th>Qualification</th><th>Speciality</th>')
for E_ID,Name,Sex,Salary,Qualification,Speciality in cursor:
    print('<tr><td>',E_ID,'</td><td>',Name,'</td><td>',Sex,'</td><td>',Salary,'</td><td>',Qualification,'</td><td>',Speciality,'</td>')
print('</table>')
print('</div>')
print('<div class="tailer"><a class="back" href="./appointment.html">Back</a></div>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
