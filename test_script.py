# Check here selenium-python doc to select elements in the DOM
# https://selenium-python.readthedocs.io/locating-elements.html

# How to get elements' absolute XPath with your browser
# https://stackoverflow.com/questions/59961926/how-to-get-absolute-xpath-in-chrome-or-firefox

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "<YOUR_URL>"

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless') # Comment this line if you want to see the browser while executing the navigation
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Test case 1 brief description"""
        try:
            self.driver.get(url)
            self.driver.set_window_size(1024, 768)
            self.driver.find_element_by_xpath('<ELEMENT_XPATH>').click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_2(self):
        """Test case 2 brief description"""
        try:
            self.driver.get(url)
            self.driver.set_window_size(1024, 768)
            self.driver.find_element_by_xpath('<ELEMENT_XPATH>').click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    
    def test_case_3(self):
        """Test case 3 brief description"""
        try:
            self.driver.get(url)
            self.driver.set_window_size(1024, 768)
            self.driver.find_element_by_xpath('<ELEMENT_XPATH>').send_keys("Lorem ipsum")
            self.driver.find_element_by_xpath('<ELEMENT_XPATH>').click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
