import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


class Typos(unittest.TestCase):
    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/typos")

    def test_find_typo(self):
        driver = self.driver
        correct_text = "Sometimes you'll see a typo, other times you won't."
        paragraph = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        tries = 1
        while correct_text != paragraph.text:
            tries += 1
            driver.refresh()
            # para que se pueda ver
            sleep(1)
            paragraph = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        print(f'Typo was find in {tries} tries')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
