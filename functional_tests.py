from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        s=Service('C:/Users/Phantom Lover/Downloads/Dev/chromedriver.exe')
        self.browser = webdriver.Chrome(service=s)

    def tearDown(self):
        return self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To Do', self.browser.title)
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
