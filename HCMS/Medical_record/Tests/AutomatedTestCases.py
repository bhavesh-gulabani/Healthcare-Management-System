import time
import unittest
import cgi
import mysql.connector as conn
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Helper function to navigate to the required form in Medical Record Module
def navigateToForm(form_name):
	driver = webdriver.Chrome('D:/Bhavesh-Data/Engineering/BE/SEM-I/STQA/Mini Project/Mini Project 2/chromedriver')	
	# Navigate to the URL
	driver.get("http://127.0.0.1/HCMS/")
	print(driver.title)
	print(driver.current_url)
	# Select Patient Medical Record Module
	time.sleep(1)
	driver.find_element_by_link_text('Medical Record').click()
	time.sleep(1)
	driver.find_element_by_link_text(form_name).click()
	time.sleep(1)
	return driver

class MedicalRecordTest(unittest.TestCase):
	def testTC7(self):
		driver = navigateToForm('Create new record')
		driver.find_element_by_name('record_no').send_keys(Keys.RETURN)
		self.assertTrue(testCase7())
		time.sleep(3)
		driver.close()
    
	def testTC8(self):
		driver = navigateToForm('Create new record')
		# Enter the values in the text boxes
		driver.find_element_by_name('record_no').send_keys("2203")
		time.sleep(1)
		driver.find_element_by_name('pat_id').send_keys('1103')
		time.sleep(1)
		driver.find_element_by_name('doc_id').send_keys('102')
		time.sleep(1)
		driver.find_element_by_name('admission_date').send_keys('01102020')
		time.sleep(1)
		driver.find_element_by_name('discharge_date').send_keys('30102020')
		time.sleep(1)
		driver.find_element_by_name('diagnosis').send_keys('Sore Throat')
		time.sleep(1)
		driver.find_element_by_name('record_no').send_keys(Keys.RETURN)
		time.sleep(1)
		self.assertTrue(testCase8())
		time.sleep(3)
		driver.close()

	def testTC9(self):
		driver = navigateToForm('Update medical record')
		driver.find_element_by_name('record_no').send_keys(Keys.RETURN)
		self.assertTrue(testCase9())
		time.sleep(3)
		driver.close()

	def testTC10(self):
		driver = navigateToForm('Update medical record')
		# Enter the values in the text boxes
		driver.find_element_by_name('record_no').send_keys("2203")
		time.sleep(1)
		driver.find_element_by_name('record_no').send_keys(Keys.RETURN)
		time.sleep(1)
		driver.find_element_by_name('doc_id').send_keys('102')
		time.sleep(1)
		driver.find_element_by_name('admission_date').send_keys('05102020')
		time.sleep(1)
		driver.find_element_by_name('discharge_date').send_keys('25102020')
		time.sleep(1)
		driver.find_element_by_name('diagnosis').send_keys('Sore Throat')
		time.sleep(1)
		driver.find_element_by_name('record_no').send_keys(Keys.RETURN)
		time.sleep(1)
		self.assertTrue(testCase10())
		time.sleep(3)
		driver.close()

# Method Calls
# MedicalRecordTest().testTC7()
# MedicalRecordTest().testTC8()
# MedicalRecordTest().testTC9()
# MedicalRecordTest().testTC10()