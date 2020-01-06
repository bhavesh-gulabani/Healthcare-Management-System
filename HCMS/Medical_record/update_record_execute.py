#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn
import webbrowser

form_data = cgi.FieldStorage()  #Fetches all the data from the form as a dictionary

record_no = form_data.getvalue('record_no')

doc_id = form_data.getvalue('doc_id')
date_admitted = form_data.getvalue('admission_date')
date_discharged = form_data.getvalue('discharge_date')
diagnosis = form_data.getvalue('diagnosis')

#print(record_no,doc_id,date_discharged,date_admitted,diagnosis)

cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
query = "update medical_record set Doctor_ID=%s,Date_admitted=%s,date_discharged=%s,Diagnosis=%s where Record_no =%s"
data = (doc_id,date_admitted,date_discharged,diagnosis,record_no,)

cursor.execute(query,data)
cnx.commit()

print('<html><head><title>Created sucessfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
print('<body><header><h1>Patient Medical Record</h1></header>')
print('<div class="message"><p>Successful!</p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
print('</body>')
print('</html>')


cursor.close()
cnx.close()
