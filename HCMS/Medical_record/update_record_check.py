#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn
import webbrowser

form_data = cgi.FieldStorage()  #Fetches all the data from the form as a dictionary

record_no = form_data.getvalue('record_no')

cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
query = "select Record_no from medical_record where Record_no = %s"

cursor.execute(query,(record_no,))
record = cursor.fetchall()

if len(record) == 1:
	query = "select P_ID from medical_record where Record_no = %s"
	cursor.execute(query,(record_no,))
	P_ID_record = cursor.fetchall()

	print('<html><head><title>Update Patient Record</title><link rel="stylesheet" type="text/css" href="../css/insert-data-style.css"></head>')
	print('<body><header><h1>Patient Medical Record</h1></header>')
	print('<div class="form-wrapper">')
	print('<form method="post" action="update_record_execute.py">')
	print('<div class="element">Record no : <input type="number" name="record_no" placeholder="Record_no" value="%s" min = "2200" max = "2299"></div><br>'%(int(record_no)))
	print('<div class="element">Patient ID : <input type="number" name="pat_id" placeholder="Patient ID" value="%s" min = "1100" max = "1199"></div><br>'%(P_ID_record[0]))
	print('<div class="element">Doctor ID : <input type="number" name="doc_id" placeholder="Doctor ID" min = "100" max = "999"></div><br>')
	print('<div class="element">Date admitted : <input type="date" name="admission_date"></div><br>')
	print('<div class="element">Date discharged : <input type="date" name="discharge_date"></div><br>')
	print('<div class="element">Diagnosis : <input type="text" name="diagnosis" placeholder="Diagnosis"></div><br>')
	print('<input type="submit" value="Register!">')
	print('<input type="reset">')
	print('</form><a href="./medical_record.html">Back</a>')
	print('</div></body></html>')
	#webbrowser.open('http://localhost/HCMS/Medical_record/update_record_execute.html',new=0)
else:
	print('<html><head><title>Created sucessfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
	print('<body><header><h1>Patient Medical Record</h1></header>')
	print('<div class="message"><p> Record not found!<br> Please re-enter</p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
	print('</body>')
	print('</html>')
cnx.commit()


cursor.close()
cnx.close()
