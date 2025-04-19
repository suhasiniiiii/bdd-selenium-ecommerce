from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        # Product-related
        self.backpack = (By.ID, "item_4_title_link")
        self.add_cart = (By.XPATH, '//*[contains(@id, "add-to-cart")]')
        self.go_cart = (By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")

        # Checkout process
        self.checkout = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_cart)
        ).click()



    def go_to_cart(self):
        self.driver.find_element(*self.go_cart).click()

    def is_product_in_cart(self, product_name):
        product_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack)
        )
        return product_element is not None

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout)
        ).click()


    def enter_first_name(self, name="Test"):
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name="User"):
        self.driver.find_element(*self.last_name).send_keys(name)

    def enter_postal_code(self, code="12345"):
        self.driver.find_element(*self.postal_code).send_keys(code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def is_checkout_overview_displayed(self):
        return "Checkout: Overview" in self.driver.page_source

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def is_order_complete(self):
        return "Thank you for your order!" in self.driver.page_source
