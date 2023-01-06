import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")
    
    def test_search_field(self):
        print('Searching the search bar')
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
    
    def test_language_option(self):
        print('Searching the Select language dropdown')
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
    
    @classmethod
    def tearDown(self):
        self.driver.quit()
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException(): 
            self.driver.close()
            return False
        return True
