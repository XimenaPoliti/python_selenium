import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# By nos permite el uso de 2 métodos privados 
# find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
# Service nos ayuda a declarar el executable_path() de nuestro webdriver.
from selenium.webdriver.chrome.service import Service


class SearchTests(unittest.TestCase):
    
    @classmethod 
    def setUpClass(cls):
        # creamos una variable s con una funcion Service('') 
        # que contiene la ruta del webdriver.
        s=Service('/usr/bin/chromedriver')
        # establecemos la referencia del driver
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, "search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button_enable(self):
        search_button = self.driver.find_element(By.CLASS_NAME, "search-button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        banners = banner_list.find_elements(By.TAG_NAME, "img")
        self.assertEqual(3, len(banners))


    def test_vip_promo(self):
        vip_promo = self.driver.find_element(
                By.XPATH,
                "//*[@id='top']/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img"
                )

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element(
                By.CSS_SELECTOR, 
                "div.header-minicart span.icon"
                )
        
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear()

        search_field.send_keys("salt shaker")
        search_field.submit()

        products = driver.find_elements(
                By.XPATH, 
                '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a'
                )
        self.assertEqual(1, len(products))

    @classmethod 
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
