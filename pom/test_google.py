import unittest
from google_page import GooglePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        service = Service('/usr/bin/chromedriver')
        cls.driver = webdriver.Chrome(service=service)

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
