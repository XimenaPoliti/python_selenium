import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


class DynamicElements(unittest.TestCase):
    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/disappearing_elements")

    def test_name_elements(self):
        driver = self.driver
        count = 1
        # se captura la cantidad de elementos li (botones)
        elements = driver.find_elements(By.XPATH, '//div[@class="example"]/ul/li')
        while len(elements) < 5:
            count += 1
            sleep(1)
            driver.refresh()
            elements = driver.find_elements(By.XPATH, '//div[@class="example"]/ul/li')

        print(f'''Se necesito refrescar el navegador {count} para que apareciera el boton dinamico''')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
