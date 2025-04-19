from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.items = (By.CLASS_NAME, "inventory_item_name")


    def filter_products(self, product_name):
        # There's no search bar on SauceDemo, so we just simulate a search
        # by checking visible product names
        pass

    def get_displayed_product_names(self):
        elements = self.driver.find_elements(*self.items)
        return [elem.text for elem in elements]

    def select_product(self,product):
        product_xpath = f"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='{product}']"
        product_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product_xpath))
        )
        product_element.click()