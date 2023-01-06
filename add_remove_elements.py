import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


class AddRemoveChallenge(unittest.TestCase):

    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    def test_add_remove_elements(self):
        add_element = int(input('How many elements will be added: '))
        remove_element = int(input('How many elements will be removed: '))
        driver = self.driver
        add_button = driver.find_element(By.XPATH,'//*[@id="content"]/div/button')
        try:
            assert add_element > remove_element, "You are trying to remove more elements than exist"
            for i in range(add_element):
                add_button.click()
            for i in range(remove_element):
                sleep(1)
                driver.find_element(By.XPATH,'//*[@id="elements"]/button').click()
        except AssertionError as error:
            print(error)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
