import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")
    
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        # limpiar barra de búsqueda
        search_field.clear() 
        # input 'tee'
        search_field.send_keys('tee')
        # enviar dato 'tee'
        search_field.submit()
    	
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear() 
        search_field.send_keys('salt shaker')
        search_field.submit()
#Searching by XPATH -> 
#$x('//div[@class = "product-info"]/h2[@class="product-name"]/a/text()').map(x => x.wholeText)
#or $x('//div[@class = "product-info"]/h2/a/text()').map(x => x.wholeText)
# REMEMBER: "h2" could also be replaced by "text-fill"
        products = driver.find_elements(
            By.XPATH, 
            '//div[@class = "product-info"]/h2[@class="product-name"]/a'
            )                                       
        self.assertEqual(1, len(products))
    
    
    @classmethod
    def tearDown(self):
        self.driver.quit()
