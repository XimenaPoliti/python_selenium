import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class DynamicControls(unittest.TestCase):
    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    def test_remove_add_button(self):
        driver = self.driver
        
        remove_button = driver.find_element(
                By.XPATH, 
                '//*[@id="checkbox-example"]/button[contains(text(),"Remove")]'
                )
        remove_button.click()
        self.validate_paragraph_text("It's gone!")

        button_add = driver.find_element(
                By.XPATH, 
                '//*[@id="checkbox-example"]/button[contains(text(),"Add")]'
                )
        button_add.click()
        self.validate_paragraph_text("It's back!")
        remove_button.click()
        self.validate_paragraph_text("It's gone!")

    def test_enable_disable(self):
        driver = self.driver

        enable_disable_button = driver.find_element(
                By.XPATH, 
                '/html/body/div[2]/div/div[1]/form[2]/button'
                )
        enable_disable_button.click()
        self.validate_paragraph_text("It's enabled!")

        enable_disable_button.click()
        self.validate_paragraph_text("It's disabled!")
        
    def validate_paragraph_text(self, expectedText):
        paragraph = self.driver.find_element(By.CSS_SELECTOR, '#message')
        paragraph_text = paragraph.text
        self.assertEqual(paragraph_text, expectedText)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
