#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn


cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
cursor.execute("select * from appointment")

print('<html><head><title>Show Appointments</title><link rel="stylesheet" type="text/css" href="../css/show-table.css"></head>')
print('<body><header><h1>Patient Appointments</h1></header>')
print('<div class="wrapper">')
print('<table><tr><th>Appointment ID</th><th>Patient ID</th><th>Doctor ID</th><th>Receptionist ID</th><th>Time</th><th>Date</th></tr>')
for appointment_id,P_ID,Doctor_ID,Receptionist_ID,Time,Date in cursor:
    print('<tr><td>',appointment_id,'</td><td>',P_ID,'</td><td>',Doctor_ID,'</td><td>',Receptionist_ID,'</td><td>',Time,'</td><td>',Date,'</td></tr>')
print('</table>')
print('</div>')
print('<div class="tailer"><a class="back" href="./appointment.html">Back</a></div>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
