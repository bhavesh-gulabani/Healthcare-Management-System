import unittest
import cgi
import mysql.connector as conn

# Test Case 11 : Patient Registration : 
# The form fields appear empty when the page is loaded
def testCase11():
	form_data = cgi.FieldStorage()
	if dict(form_data) == {} :
		return True
	return False

# Test Case 12 : Patient Registration : 
# To check whether correct data is entered into the relevant fields/text boxes
def testCase12():
	form_data = cgi.FieldStorage()	
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

	if pat_id != None and name != None and gender != None and dob != None and age != None and email != None and addr != None:
		return True
	return False

class PatientRegistrationTest(unittest.TestCase):
    def testTC11(self):
        self.assertTrue(testCase11())
    
    def testTC12(self):
    	self.assertTrue(testCase12())
