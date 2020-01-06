#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn

form_data = cgi.FieldStorage()  #Fetches all the data from the form as a dictionary

appointment_id = form_data.getvalue('appointment_id')
pat_id = form_data.getvalue('pat_id')
doc_id = form_data.getvalue('doc_id')
rec_id = form_data.getvalue('rec_id')
time = form_data.getvalue('Time')
date = form_data.getvalue('Date')
entereddate = str(date).split('-')


from datetime import date as dt
today = dt.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
todaysdate = d1.split('/')

if int(entereddate[0]) < int(todaysdate[2]):
    print('insside1')
    print('<html><head><title>Booked Successfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>New Patient Appointment</h1></header>')
    print('<div class="message"><p> PLEASE ENTER VALID DATE!</p><div class="previous"><a href="./appointment.html">Back</a></div></div>')
    print('</body>')
    print('</html>')
elif int(entereddate[1]) < int(todaysdate[1]):
    print('insside2')
    print('<html><head><title>Booked Successfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>New Patient Appointment</h1></header>')
    print('<div class="message"><p> PLEASE ENTER VALID DATE!</p><div class="previous"><a href="./appointment.html">Back</a></div></div>')
    print('</body>')
    print('</html>')
elif int(entereddate[2]) < int(todaysdate[0]):
    print('insside3')
    print('<html><head><title>Booked Successfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>New Patient Appointment</h1></header>')
    print('<div class="message"><p> PLEASE ENTER VALID DATE!</p><div class="previous"><a href="./appointment.html">Back</a></div></div>')
    print('</body>')
    print('</html>')
else:
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
