"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case1(self):
        """Find and click top-right button"""
        try:
            self.driver.get('https://www.oursky.com/')
            el = self.driver.find_element_by_class_name('btn-header')
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case2(self):
        """Find and click Learn more button"""
        try:
            self.driver.get('https://www.oursky.com/')
            el = self.driver.find_element_by_xpath(".//*[@id='tag-line-wrap']/span/a")
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
