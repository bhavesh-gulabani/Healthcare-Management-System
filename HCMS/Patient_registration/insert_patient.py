#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn
from Tests.TestCases import *

def printTestCaseResult(status, number):
    print(f'<html><head><title>Patient Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print(f'<body><header><h1>Test Case {number}</h1></header>')
    print(f'<div class="message"><p> {status} </p><div class="previous"><a href="../index.html">Back</a></div></div>')
    print(f'</body>')
    print(f'</html>')

# Testing TC11 : The form fields appear empty when the page is loaded
# try :
#     PatientRegistrationTest().testTC11()
# except AssertionError:
#     printTestCaseResult('Failed', 11)
# else:
#     printTestCaseResult('Passed', 11)

# Testing TC12 : To check whether correct data is entered into the relevant fields/text boxes
# try :
#     PatientRegistrationTest().testTC12()
# except AssertionError:
#     printTestCaseResult('Failed', 12)
# else:
#     printTestCaseResult('Passed', 12)

form_data = cgi.FieldStorage()         
pat_id = form_data.getvalue('pat_id')
name = form_data.getvalue('name')
if form_data.getvalue('gender'):
    gender = form_data.getvalue('gender')
else:
    gender = "Not selected"
dob = form_data.getvalue('DOB')
age  = form_data.getvalue('age')
email  = form_data.getvalue('email')
if form_data.getvalue('address'):
    addr = form_data.getvalue('address')
else:
    addr = "Not entered"
agecheck = int(age)


cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
add_patient = ("INSERT INTO patient VALUES (%s,%s,%s,%s,%s,%s,%s)")
data_patient = (int(pat_id),name,gender,dob,int(age),email,addr)
cursor.execute(add_patient,data_patient)
cnx.commit()

print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
print('<body><header><h1>Patient Registration</h1></header>')
print('<div class="message"><p> Successful!</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
print('</body>')
print('</html>')
cursor.close()
cnx.close()