#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn


cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
cursor.execute("select * from medical_record")

print('<html><head><title>Show Medical Records</title><link rel="stylesheet" type="text/css" href="../css/show-table.css"></head>')
print('<body><header><h1>Patient Medical Records</h1></header>')
print('<div class="wrapper">')
print('<table><tr><th>Record No</th><th>Patient ID</th><th>Doctor ID</th><th>Date admitted</th><th>Date discharged</th><th>Diagnosis</th></tr>')
for Record_no,P_ID,Doctor_ID,Date_admitted,Date_discharged,Diagnosis in cursor:
    print('<tr><td>',Record_no,'</td><td>',P_ID,'</td><td>',Doctor_ID,'</td><td>',Date_admitted,'</td><td>',Date_discharged,'</td><td>',Diagnosis,'</td></tr>')
print('</table>')
print('</div>')
print('<div class="tailer"><a class="back" href="./medical_record.html">Back</a></div>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
