import unittest
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Tables(unittest.TestCase):
    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

    def test_table(self):
        driver = self.driver
        rows = []
        ptable = PrettyTable()
        for i in range(5):
            header = driver.find_element(
                By.XPATH, 
                f'//*[@id="table1"]/thead/tr/th[{i+1}]/span'
                )
            for j in range(4):
                row = driver.find_element(
                    By.XPATH,
                    f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]'
                    )
                rows.append(row.text)
            ptable.add_column(header.text, rows)
            rows.clear()

        print('\n', ptable)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

