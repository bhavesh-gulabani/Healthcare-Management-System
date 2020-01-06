#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn

form_data = cgi.FieldStorage()  #Fetches all the data from the form as a dictionary


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
