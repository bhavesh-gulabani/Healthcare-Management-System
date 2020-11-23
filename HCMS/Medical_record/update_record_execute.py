#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn
import webbrowser
from Tests.TestCases import *

def printTestCaseResult(status, number):
    print(f'<html><head><title>Generate Receipt</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print(f'<body><header><h1>Test Case {number}</h1></header>')
    print(f'<div class="message"><p> {status} </p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
    print(f'</body>')
    print(f'</html>')

# Testing TC9 : The form fields appear empty when the page is loaded
# try :
#     MedicalRecordTest().testTC9()
# except AssertionError:
#     printTestCaseResult('Failed', 9)
# else:
#     printTestCaseResult('Passed', 9)

# Testing TC10 : To check whether correct data is entered into the relevant fields/text boxes
# try :
#     MedicalRecordTest().testTC10()
# except AssertionError:
#     printTestCaseResult('Failed', 10)
# else:
#     printTestCaseResult('Passed', 10)

form_data = cgi.FieldStorage()  
record_no = form_data.getvalue('record_no')
doc_id = form_data.getvalue('doc_id')
date_admitted = form_data.getvalue('admission_date')
date_discharged = form_data.getvalue('discharge_date')
diagnosis = form_data.getvalue('diagnosis')


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
