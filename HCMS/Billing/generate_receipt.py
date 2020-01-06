#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn

form_data = cgi.FieldStorage()  #Fetches all the data from the form as a dictionary

receipt_id = form_data.getvalue('receipt_id')
pat_id = form_data.getvalue('pat_id')
mode_of_payment = form_data.getvalue('Mode_of_payment')
amount = form_data.getvalue('Amount')
status = form_data.getvalue('Status')

cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')

cursor = cnx.cursor()

add_record = ("INSERT INTO billing VALUES (%s,%s,%s,%s,%s)")
data_record = (int(receipt_id),int(pat_id),mode_of_payment,int(amount),status)

cursor.execute(add_record,data_record)

cnx.commit()
print('<html><head><title>Generated Successfully</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
print('<body><header><h1>Payment Receipt</h1></header>')
print('<div class="message"><p> Successful!</p><div class="previous"><a href="./billing.html">Back</a></div></div>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
