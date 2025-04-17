from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators based on saucedemo.com
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.inventory_container = (By.ID, "inventory_container")  # this appears only after login
        self.error_message = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")


    def load(self, base_url):
        self.driver.get(base_url)

    def enter_username(self,username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.inventory_container)
            )
            return True
        except:
            return False

    def is_login_failed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.error_message)
            )

            return True
        except:
            return False
