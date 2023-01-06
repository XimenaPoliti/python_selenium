import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        exp_option = ['English', 'French', 'German']
        
        # Toma los elementos con Select del drop down y las añade a act_options
        select_language = Select(self.driver.find_element('id', 'select-language'))
        self.assertEqual(3, len(select_language.options))
        
        act_options = [i.text for i in select_language.options]

        # Verifica que las listas sean iguales
        self.assertListEqual(exp_option, act_options)
        
        # Validar que inglés sea el idioma seleccionado por defecto
        self.assertEqual('English', select_language.first_selected_option.text)
    
        # Selecciona alemán como idioma por el texto visible
        select_language.select_by_visible_text('German')
    
        # Verifica el cambio viendo parte del url
        self.assertTrue('store=german' in self.driver.current_url)
    
        # Selecciona de nuevo el inglés por el indice
        select_language = Select(self.driver.find_element('id', 'select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
