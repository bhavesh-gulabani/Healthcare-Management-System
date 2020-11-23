#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python
print("Content-type: text/html")
print()

import cgi
import mysql.connector as conn
from Tests.TestCases import *

def printTestCaseResult(status, number):
	print(f'<html><head><title>Generate Receipt</title><link rel="stylesheet" type="text/css" href="../css/successful-insert.css"></head>')
	print(f'<body><header><h1>Test Case {number}</h1></header>')
	print(f'<div class="message"><p> {status} </p><div class="previous"><a href="./billing.html">Back</a></div></div>')
	print(f'</body>')
	print(f'</html>')

# Testing TC1 : The form fields appear empty when the page is loaded
# try:
# 	BillingTest().testTC1()
# except AssertionError:
# 	printTestCaseResult('Failed', 1)
# else:
# 	printTestCaseResult('Passed', 1)

# Testing TC2 : To check whether correct data is entered into the relevant fields/text boxes
# try:
# 	BillingTest().testTC2()
# except AssertionError:
# 	printTestCaseResult('Failed', 2)
# else:
# 	printTestCaseResult('Passed', 2)

form_data = cgi.FieldStorage()
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