#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn

cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()

form_data = cgi.FieldStorage()  #Fetches all the data from the form as a dictionary
app_id = form_data.getvalue('appointment_id')

query = "select Appointment_ID from appointment where Appointment_ID = %s"
cursor.execute(query,(app_id,))
record = cursor.fetchall()

if len(record) == 1:

	query="delete from appointment where Appointment_ID=%s"

	cursor.execute(query,(app_id,))

	cnx.commit()

	print('<html><head><title>Cancellation Successful</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
	print('<body><header><h1>Cancel Appointment</h1></header>')
	print('<div class="message"><p> Successful!</p><div class="previous"><a href="./appointment.html">Back</a></div></div>')
	print('</body>')
	print('</html>')
else:
	print('<html><head><title>Not found</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
	print('<body><header><h1>Cancel Appointment</h1></header>')
	print('<div class="message"><p> Appointment not found!<br> Please re-enter</p><div class="previous"><a href="./cancel_appointment.html">Back</a></div></div>')
	print('</body>')
	print('</html>')

cursor.close()
cnx.close()
