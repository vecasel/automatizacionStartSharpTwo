import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LoginPage:
    """Página de inicio de sesión"""

    URL = "https://serenity.is/demo/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(LoginPage.URL)

    def login(self, username, password):
        username_field = self.driver.find_element(By.NAME, "Username")
        password_field = self.driver.find_element(By.NAME, "Password")
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)


class DashboardPage:
    """Página del panel de control"""

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_icons(self):
        return self.driver.find_elements(By.XPATH, "//*[contains(@class, \"fa\")]")

    def get_buttons(self):
        return self.driver.find_elements(By.XPATH, "//*[contains(@class, \"icon\")]")

    def get_text_fields(self):
        return self.driver.find_elements(By.TAG_NAME, "input")

    def get_images(self):
        return self.driver.find_elements(By.TAG_NAME, "img")

    def get_heading(self):
        return self.driver.find_element(By.TAG_NAME, "h1")


class TestInterfaz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_visualizacion_interfaz(self):
        # Ingresar las credenciales de usuario y contraseña
        self.login_page.load()
        self.login_page.login("admin", "serenity")
        time.sleep(2)

        # Verificar la visualización correcta de los elementos de la interfaz
        self.assertEqual("Dashboard - StartSharp", self.dashboard_page.get_title())
        iconos = self.dashboard_page.get_icons()
        self.assertTrue(len(iconos) > 0)
        botones = self.dashboard_page.get_buttons()
        self.assertTrue(len(botones) > 0)
        campos_texto = self.dashboard_page.get_text_fields()
        self.assertTrue(len(campos_texto) > 0)
        imagenes = self.dashboard_page.get_images()
        self.assertTrue(len(imagenes) > 0)
        titulo = self.dashboard_page.get_heading()
        self.assertTrue(titulo.is_displayed())


if __name__ == '__main__':
    unittest.main()
