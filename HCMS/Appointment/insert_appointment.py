#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn
from Tests.TestCases import *

def printTestCaseResult(status, number):
	print(f'<html><head><title>Generate Receipt</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
	print(f'<body><header><h1>Test Case {number}</h1></header>')
	print(f'<div class="message"><p> {status} </p><div class="previous"><a href="./appointment.html">Back</a></div></div>')
	print(f'</body>')
	print(f'</html>')

# Testing TC3 : The form fields appear empty when the page is loaded
# try:
# 	AppointmentTest().testTC3()
# except AssertionError:
# 	printTestCaseResult('Failed', 3)
# else:
# 	printTestCaseResult('Passed', 3)

# Testing TC4 : To check whether correct data is entered into the relevant fields/text boxes
# try:
# 	AppointmentTest().testTC4()
# except AssertionError:
# 	printTestCaseResult('Failed', 4)
# else:
# 	printTestCaseResult('Passed', 4)

form_data = cgi.FieldStorage()
appointment_id = form_data.getvalue('appointment_id')
pat_id = form_data.getvalue('pat_id')
doc_id = form_data.getvalue('doc_id')
rec_id = form_data.getvalue('rec_id')
time = form_data.getvalue('Time')
date = form_data.getvalue('Date')
entereddate = str(date).split('-')

cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')

cursor = cnx.cursor()

add_record = ("INSERT INTO appointment VALUES (%s,%s,%s,%s,%s,%s)")
data_record = (int(appointment_id),int(pat_id),int(doc_id),int(rec_id),time,date)

cursor.execute(add_record,data_record)

cnx.commit()
print('<html><head><title>Booked Successfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
print('<body><header><h1>New Patient Appointment</h1></header>')
print('<div class="message"><p> Successful!</p><div class="previous"><a href="./appointment.html">Back</a></div></div>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
