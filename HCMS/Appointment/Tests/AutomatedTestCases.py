import time
import unittest
import cgi
import mysql.connector as conn
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Helper function to navigate to the required form in Appointment Module
def navigateToForm(form_name):
	driver = webdriver.Chrome('D:/Bhavesh-Data/Engineering/BE/SEM-I/STQA/Mini Project/Mini Project 2/chromedriver')	
	# Navigate to the URL
	driver.get("http://127.0.0.1/HCMS/")
	print(driver.title)
	print(driver.current_url)
	# Select Patient Appointment Module
	time.sleep(1)
	driver.find_element_by_link_text('Appointment Section').click()
	time.sleep(1)
	driver.find_element_by_link_text(form_name).click()
	time.sleep(1)
	return driver

class AppointmentTest(unittest.TestCase):
	def testTC3(self):
		driver = navigateToForm('Book Appointment')
		driver.find_element_by_name('appointment_id').send_keys(Keys.RETURN)
		self.assertTrue(testCase3())
		time.sleep(3)
		driver.close()
    
	def testTC4(self):
		driver = navigateToForm('Book Appointment')
		# Enter the values in the text boxes
		driver.find_element_by_name('appointment_id').send_keys("3303")
		time.sleep(1)
		driver.find_element_by_name('pat_id').send_keys('1103')
		time.sleep(1)
		driver.find_element_by_name('doc_id').send_keys('102')
		time.sleep(1)
		driver.find_element_by_name('rec_id').send_keys('103')
		time.sleep(1)
		driver.find_element_by_name('Time').send_keys('0900')
		time.sleep(1)
		driver.find_element_by_name('Date').send_keys('01102020')
		time.sleep(1)
		driver.find_element_by_name('appointment_id').send_keys(Keys.RETURN)
		time.sleep(1)
		self.assertTrue(testCase4())
		time.sleep(3)
		driver.close()

	def testTC5(self):
		driver = navigateToForm('Cancel Appointment')
		driver.find_element_by_name('appointment_id').send_keys(Keys.RETURN)
		self.assertTrue(testCase5())
		time.sleep(3)
		driver.close()

	def testTC6(self):
		driver = navigateToForm('Cancel appointment')
		# Enter the values in the text boxes
		driver.find_element_by_name('appointment_id').send_keys("3303")
		time.sleep(1)
		driver.find_element_by_name('appointment_id').send_keys(Keys.RETURN)
		time.sleep(1)
		self.assertTrue(testCase6())
		time.sleep(3)
		driver.close()

# Method Calls
# AppointmentTest().testTC3()
# AppointmentTest().testTC4()
# AppointmentTest().testTC5()
# AppointmentTest().testTC6()
