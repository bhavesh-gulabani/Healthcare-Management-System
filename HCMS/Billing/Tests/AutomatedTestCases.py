import time
import unittest
import cgi
import mysql.connector as conn
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Helper function to navigate to Patient Registration Form
def navigateToForm():
	driver = webdriver.Chrome('D:/Bhavesh-Data/Engineering/BE/SEM-I/STQA/Mini Project/Mini Project 2/chromedriver')	
	# Navigate to the URL
	driver.get("http://127.0.0.1/HCMS/")
	print(driver.title)
	print(driver.current_url)
	# Select Billing Module
	time.sleep(1)
	driver.find_element_by_link_text('Billing Section').click()
	time.sleep(1)
	driver.find_element_by_link_text('Generate receipt').click()
	time.sleep(1)
	return driver

class BillingTest(unittest.TestCase):
	def testTC1(self):
		driver = navigateToForm()
		driver.find_element_by_name('receipt_id').send_keys(Keys.RETURN)
		self.assertTrue(testCase1())
		time.sleep(3)
		driver.close()
    
	def testTC2(self):
		driver = navigateToForm()
		# Enter the values in the text boxes
		driver.find_element_by_name('receipt_id').send_keys("4403")
		time.sleep(1)
		driver.find_element_by_name('pat_id').send_keys('1103')
		time.sleep(1)
		driver.find_element_by_name('Mode_of_payment').send_keys('Cash')
		time.sleep(1)
		driver.find_element_by_name('Amount').send_keys('20000')
		time.sleep(1)
		driver.find_element_by_name('Status').send_keys('Paid')
		time.sleep(1)
		driver.find_element_by_name('receipt_id').send_keys(Keys.RETURN)
		time.sleep(1)
		self.assertTrue(testCase2())
		time.sleep(3)
		driver.close()

# Method Calls
# BillingTest().testTC1()
# BillingTest().testTC2()