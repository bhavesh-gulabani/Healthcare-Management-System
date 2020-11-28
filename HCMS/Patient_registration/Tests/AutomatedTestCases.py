import time
import unittest
import cgi
import mysql.connector as conn
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Helper function to navigate to Patient Registration Form
def navigateToForm():
	driver = webdriver.Chrome('D:/Bhavesh-Data/Engineering/BE/SEM-I/STQA/Mini Project/Mini Project 2/chromedriver')	
	# Navigate to the URL
	driver.get("http://127.0.0.1/HCMS/")
	print(driver.title)
	print(driver.current_url)
	# Select Patient Registration Module
	time.sleep(1)
	driver.find_element_by_link_text('Register Patient').click()
	time.sleep(1)
	return driver

class PatientRegistrationTest(unittest.TestCase):

	def testTC11(self):
		driver = navigateToForm()
		driver.find_element_by_name('pat_id').send_keys(Keys.RETURN)
		self.assertTrue(testCase11())
		time.sleep(3)
		driver.close()

	def testTC12(self):
		driver = navigateToForm()

		# Enter the values in the text boxes
		driver.find_element_by_name('pat_id').send_keys("1103")
		time.sleep(1)
		driver.find_element_by_name('name').send_keys('Johnny')
		time.sleep(1)
		driver.find_elements_by_css_selector('input[type="radio"][value="Male"]')[0].click()
		time.sleep(1)
		driver.find_element_by_name('DOB').send_keys('01011999')
		time.sleep(1)
		driver.find_element_by_name('age').send_keys('20')
		time.sleep(1)
		driver.find_element_by_name('email').send_keys('Johnny@gmail.com')
		time.sleep(1)
		driver.find_element_by_name('address').send_keys('First Avenue, New York')
		time.sleep(1)
		driver.find_element_by_name('pat_id').send_keys(Keys.RETURN)
		time.sleep(1)
		self.assertTrue(testCase12())
		time.sleep(3)
		driver.close()

# Method Calls
# PatientRegistrationTest().testTC11()
# PatientRegistrationTest().testTC12()