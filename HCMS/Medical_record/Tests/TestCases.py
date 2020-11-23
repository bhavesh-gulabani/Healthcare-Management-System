import unittest
import cgi
import mysql.connector as conn

# Test Case 7 : Medical Record Section : Create Medical Record : 
# The form fields appear empty when the page is loaded
def testCase7():
	form_data = cgi.FieldStorage()
	if dict(form_data) == {} :
		return True
	return False

# Test Case 8 : Medical Record Section : Create Medical Record : 
# To check whether correct data is entered into the relevant fields/text boxes
def testCase8():
	form_data = cgi.FieldStorage()	
	record_no = form_data.getvalue('record_no')
	pat_id = form_data.getvalue('pat_id')
	doc_id = form_data.getvalue('doc_id')
	date_admitted = form_data.getvalue('admission_date')
	date_discharged = form_data.getvalue('discharge_date')
	diagnosis = form_data.getvalue('diagnosis')

	if record_no != None and pat_id != None and doc_id != None and date_admitted != None and date_discharged != None and diagnosis != None:
		return True
	return False

# Test Case 9 : Medical Record Section : Update Medical Record : 
# The form fields appear empty when the page is loaded
def testCase9():
	form_data = cgi.FieldStorage()
	if dict(form_data) == {} :
		return True
	return False

# Test Case 10 : Medical Record Section : Update Medical Record : 
# To check whether correct data is entered into the relevant fields/text boxes
def testCase10():
	form_data = cgi.FieldStorage()	
	record_no = form_data.getvalue('record_no')
	doc_id = form_data.getvalue('doc_id')
	date_admitted = form_data.getvalue('admission_date')
	date_discharged = form_data.getvalue('discharge_date')
	diagnosis = form_data.getvalue('diagnosis')

	if record_no != None and doc_id != None and date_admitted != None and date_discharged != None and diagnosis != None:
		return True
	return False

class MedicalRecordTest(unittest.TestCase):
    def testTC7(self):
        self.assertTrue(testCase7())
    
    def testTC8(self):
    	self.assertTrue(testCase8())

    def testTC9(self):
        self.assertTrue(testCase9())
    
    def testTC10(self):
    	self.assertTrue(testCase10())