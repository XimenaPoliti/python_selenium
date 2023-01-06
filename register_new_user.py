import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://demo-store.seleniumacademy.com/')
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

    def test_new_user(self):
        driver = self.driver
        try:
            #le decimos al driver que encuentre la opción de cuenta por su Xpath y
            # haga click para desplegar el menu
            driver.find_element(
                    By.XPATH, 
                    '//*[@id="header"]/div/div[2]/div/a/span[2]'
                    ).click()
            #el driver va a buscar el enlace por su texto y haga click
            driver.find_element(By.LINK_TEXT, 'Log In').click()
            #creo una variable asociada al botón de crear cuenta
            create_account_button = driver.find_element(
                    By.XPATH,
                    '//*[@id="login-form"]/div/div[1]/div[2]/a'
                    )
            #validamos que el botón esté visible y habilitado
            self.assertTrue(
                    create_account_button.is_displayed() and create_account_button.is_enabled()
                    )
            create_account_button.click()
            #comprueba que estamos en el sitio de crear cuenta
            self.assertEqual('Create New Customer Account', driver.title)
            #creación de variables con el nombre del selector correspondiente
            elements = {
                    "first_name": driver.find_element(By.ID, 'firstname'),
                    "last_name": driver.find_element(By.ID, 'lastname'),
                    "email_address": driver.find_element(By.ID, 'email_address'),
                    "password": driver.find_element(By.ID, 'password'),
                    "confirm_password": driver.find_element(By.ID, 'confirmation'),
                    "is_subscribed": driver.find_element(By.ID, 'is_subscribed'),
                    "submit_button": driver.find_element(
                        By.XPATH, 
                        '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')
                        }
            #veremos si los elementos están habilitados        
            for value in elements.values():
                self.assertTrue(value.is_enabled())

            #mandamos los datos al formulario
            for key, val in elements.items():
                if key == 'email_address':
                    val.send_keys('Test@testing.com')
                    continue
                if key == 'is_subscribed':
                    continue
                if key == 'submit_button':
                    val.click()
                    break
                val.send_keys('Test')

        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
