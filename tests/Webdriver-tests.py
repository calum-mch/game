from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import unittest
import os
import requests

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS(service_log_path=os.path.devnull)

    def test_selenium_hello_world(self):
        self.driver.get("http://www.google.com")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("cheese")
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.ID,'resultStats')))
        assert self.driver.title == "cheese - Google Search"

	def test_website_is_up(self):
		try:
			r = requests.head("http://stackoverflow.com")
			c = r.status_code
		except requests.ConnectionError:
			c = "failed to connect"
		assert c == 200
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    testResult = unittest.main() 

