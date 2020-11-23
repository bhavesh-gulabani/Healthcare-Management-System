#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn
from Tests.TestCases import *

def printTestCaseResult(status, number):
    print(f'<html><head><title>Generate Receipt</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print(f'<body><header><h1>Test Case {number}</h1></header>')
    print(f'<div class="message"><p> {status} </p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
    print(f'</body>')
    print(f'</html>')

# Testing TC7 : The form fields appear empty when the page is loaded
# try :
#     MedicalRecordTest().testTC7()
# except AssertionError:
#     printTestCaseResult('Failed', 7)
# else:
#     printTestCaseResult('Passed', 7)

# Testing TC8 : To check whether correct data is entered into the relevant fields/text boxes
# try :
#     MedicalRecordTest().testTC8()
# except AssertionError:
#     printTestCaseResult('Failed', 8)
# else:
#     printTestCaseResult('Passed', 8)

form_data = cgi.FieldStorage()  
record_no = form_data.getvalue('record_no')
pat_id = form_data.getvalue('pat_id')
doc_id = form_data.getvalue('doc_id')
date_admitted = form_data.getvalue('admission_date')
date_discharged = form_data.getvalue('discharge_date')
diagnosis = form_data.getvalue('diagnosis')

admitdate = list(map(int,str(date_admitted).split('-')))
dischargedate = list(map(int,str(date_discharged).split('-')))


if admitdate[0] > dischargedate[0]:
    print('<html><head><title>Created sucessfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>Patient Medical Record</h1></header>')
    print('<div class="message"><p> Please Enter a discharge date that is after the admission date!</p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
    print('</body>')
    print('</html>')
elif admitdate[1] > dischargedate[1]:
    print('<html><head><title>Created sucessfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>Patient Medical Record</h1></header>')
    print('<div class="message"><p> Please Enter a discharge date that is after the admission date!</p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
    print('</body>')
    print('</html>')
elif admitdate[2] > dischargedate[2]:
    print('<html><head><title>Created sucessfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>Patient Medical Record</h1></header>')
    print('<div class="message"><p> Please Enter a discharge date that is after the admission date!</p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
    print('</body>')
    print('</html>')
else:
    cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')

    cursor = cnx.cursor()

    add_record = ("INSERT INTO medical_record VALUES (%s,%s,%s,%s,%s,%s)")
    data_record = (int(record_no),int(pat_id),int(doc_id),date_admitted,date_discharged,diagnosis)

    cursor.execute(add_record,data_record)

    cnx.commit()
    print('<html><head><title>Created sucessfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>Patient Medical Record</h1></header>')
    print('<div class="message"><p> Successful!</p><div class="previous"><a href="./medical_record.html">Back</a></div></div>')
    print('</body>')
    print('</html>')
    cursor.close()
    cnx.close()
