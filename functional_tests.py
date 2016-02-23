from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def test_can_start_a_lis_and_retrieve_it_later(self):
		# Check out the to do app
		self.browser.get('http://localhost:8000')

		# The page title and the header mention to-do lists
		self.assertIn('To-do', self.browser.title)
		self.fail('Finish the test')

		# Enter a to-do item straight away

		# Types 'Buy peacock feathers' into a text box

		# Hits enter and the page updates and lists "1: Buy peacock feathers"
		# as a item i a to-do list

		# There is still a textbox to add another item
		# Enter "Use peacock feathers to make a fly"

		# The page updates agains and shows another item on the list

		# The site generates a unique url for a user to remember lists

		# Visit tha url and see the to-do list

		# User satisfied

	def tearDown(self):		
		self.browser.quit()

if __name__ == '__main__':
	unittest.main(warnings='ignore')
