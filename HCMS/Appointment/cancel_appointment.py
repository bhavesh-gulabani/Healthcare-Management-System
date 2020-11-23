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

# Testing TC5 : The form fields appear empty when the page is loaded
# try:
# 	AppointmentTest().testTC5()
# except AssertionError:
# 	printTestCaseResult('Failed', 5)
# else:
# 	printTestCaseResult('Passed', 5)

# Testing TC6 : To check whether correct data is entered into the relevant fields/text boxes
# try:
# 	AppointmentTest().testTC6()
# except AssertionError:
# 	printTestCaseResult('Failed', 6)
# else:
# 	printTestCaseResult('Passed', 6)

cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()

form_data = cgi.FieldStorage()  
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
