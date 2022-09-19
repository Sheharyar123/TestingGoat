from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        s=Service('C:/Users/Phantom Lover/Downloads/Dev/chromedriver.exe')
        self.browser = webdriver.Chrome(service=s)

    def tearDown(self):
        return self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Selenium's way of typing into input elements
        inputbox.send_keys('Buy peacock feathers')

        # Keys lets us send special keys like ENTER to the browser
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item didn't appear in table"
        )

        self.fail('Finish the test')



if __name__ == '__main__':
    unittest.main()
