import unittest
import cgi
import mysql.connector as conn

# Test Case 1 : For the Billing Section :
# The form fields appear empty when the page is loaded
def testCase1():
	form_data = cgi.FieldStorage()
	if dict(form_data) == {} :
		return True
	return False

# Test Case 2 : For the Billing Section : 
# To check whether correct data is entered into the relevant fields/text boxes
def testCase2():
	form_data = cgi.FieldStorage()	
	receipt_id = form_data.getvalue('receipt_id')
	pat_id = form_data.getvalue('pat_id')
	mode_of_payment = form_data.getvalue('Mode_of_payment')
	amount = form_data.getvalue('Amount')
	status = form_data.getvalue('Status')

	if receipt_id != None and pat_id != None and mode_of_payment != None and amount != None and status != None:
		return True
	return False

class BillingTest(unittest.TestCase):
    def testTC1(self):
        self.assertTrue(testCase1())
    
    def testTC2(self):
    	self.assertTrue(testCase2())
