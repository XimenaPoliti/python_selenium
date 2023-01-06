import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class CompareProducts(unittest.TestCase):

    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('Platzi')
        search_field.submit()
        driver.back()
        driver.implicitly_wait(3)
        driver.forward()
        driver.implicitly_wait(3)
        driver.refresh()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
