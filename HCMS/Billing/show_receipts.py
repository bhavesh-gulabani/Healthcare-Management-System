#!C:\Users\Bhavesh\AppData\Local\Programs\Python\Python37-32\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn


cnx = conn.connect(user='root',host='127.0.0.1',database='hospital')
cursor = cnx.cursor()
cursor.execute("select * from billing")

print('<html><head><title>Show Receipts</title><link rel="stylesheet" type="text/css" href="../css/show-table.css"></head>')
print('<body><header><h1>Payment receipts</h1></header>')
print('<div class="wrapper">')
print('<table><tr><th>Receipt ID</th><th>Patient ID</th><th>Mode of payment</th><th>Amount</th><th>Status</th></tr>')
for Receipt_ID,P_ID,Mode_of_payment,Amount,Status in cursor:
    print('<tr><td>',Receipt_ID,'</td><td>',P_ID,'</td><td>',Mode_of_payment,'</td><td>',Amount,'</td><td>',Status,'</td></tr>')
print('</table>')
print('</div>')
print('<div class="tailer"><a class="back" href="./billing.html">Back</a></div>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
