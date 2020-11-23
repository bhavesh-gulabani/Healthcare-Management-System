import unittest
import cgi
import mysql.connector as conn

# Test Case 3 : For Appointment Section : Book Appointment : 
# The form fields appear empty when the page is loaded
def testCase3():
	form_data = cgi.FieldStorage()
	if dict(form_data) == {} :
		return True
	return False

# Test Case 4 : For Appointment Section : Book Appointment : 
# To check whether correct data is entered into the relevant fields/text boxes
def testCase4():
	form_data = cgi.FieldStorage()
	appointment_id = form_data.getvalue('appointment_id')
	pat_id = form_data.getvalue('pat_id')
	doc_id = form_data.getvalue('doc_id')
	rec_id = form_data.getvalue('rec_id')
	time = form_data.getvalue('Time')
	date = form_data.getvalue('Date')

	if appointment_id != None and pat_id != None and doc_id != None and rec_id != None and time != None and date != None:
		return True
	return False

# Test Case 5 : For Appointment Section : Cancel Appointment : 
# The form fields appear empty when the page is loaded
def testCase5():
	form_data = cgi.FieldStorage()
	if dict(form_data) == {} :
		return True
	return False

# Test Case 6 : For Appointment Section : Cancel Appointment : 
# To check whether correct data is entered into the relevant fields/text boxes
def testCase6():
	form_data = cgi.FieldStorage()
	app_id = form_data.getvalue('appointment_id')
	if app_id != None:
		return True
	return False

class AppointmentTest(unittest.TestCase):
    def testTC3(self):
        self.assertTrue(testCase3())
    
    def testTC4(self):
    	self.assertTrue(testCase4())

    def testTC5(self):
    	self.assertTrue(testCase5())

    def testTC6(self):
    	self.assertTrue(testCase6())
