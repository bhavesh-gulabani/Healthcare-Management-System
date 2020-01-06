#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn

form_data = cgi.FieldStorage()  #Fetches all the data from the form as a dictionary

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


entereddate1 = list(str(dob).split('-'))
from datetime import date as dt
today = dt.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
todaysdate = d1.split('/')

if (int(entereddate1[0]) < int(todaysdate[2])):
    if agecheck > (int(todaysdate[2]) - int(entereddate1[0])):
        print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
        print('<body><header><h1>Patient Registration</h1></header>')
        print('<div class="message"><p> ENTER VALID AGE</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
        print('</body>')
        print('</html>')
    else:
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
elif (int(entereddate1[0]) == int(todaysdate[2]) and (int(entereddate1[1] < int(todaysdate[1])))):
    if agecheck > (int(todaysdate[2]) - int(entereddate1[0])):
        print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
        print('<body><header><h1>Patient Registration</h1></header>')
        print('<div class="message"><p> ENTER VALID AGE</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
        print('</body>')
        print('</html>')
    else:
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
elif (int(entereddate1[0]) == int(todaysdate[2]) and (int(entereddate1[1] == int(todaysdate[1]))) and int(entereddate1[2] < int(todaysdate[0]))):
    if agecheck > (int(todaysdate[2]) - int(entereddate1[0])):
        print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
        print('<body><header><h1>Patient Registration</h1></header>')
        print('<div class="message"><p> ENTER VALID AGE</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
        print('</body>')
        print('</html>')
    else:
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
elif (int(entereddate1[0]) == int(todaysdate[2]) and (int(entereddate1[1] == int(todaysdate[1]))) and int(entereddate1[2] == int(todaysdate[0]))):
    if agecheck > (int(todaysdate[2]) - int(entereddate1[0])):
        print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
        print('<body><header><h1>Patient Registration</h1></header>')
        print('<div class="message"><p> ENTER VALID AGE</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
        print('</body>')
        print('</html>')
    else:
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

elif int(entereddate1[0]) > int(todaysdate[2]):
    print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>Patient Registration</h1></header>')
    print('<div class="message"><p> ENTER VALID DATE OF BIRTH</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
    print('</body>')
    print('</html>')
elif int(entereddate1[1]) > int(todaysdate[1]):
    print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>Patient Registration</h1></header>')
    print('<div class="message"><p> ENTER VALID DATE OF BIRTH</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
    print('</body>')
    print('</html>')
elif int(entereddate1[2]) > int(todaysdate[0]):
    print('<html><head><title>Successful Registration</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
    print('<body><header><h1>Patient Registration</h1></header>')
    print('<div class="message"><p> ENTER VALID DATE OF BIRTH</p><div class="previous"><a href="../index.html">Go to homepage</a></div></div>')
    print('</body>')
    print('</html>')
