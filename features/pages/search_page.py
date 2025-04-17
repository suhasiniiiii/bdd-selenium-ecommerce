from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_products(self, product_name):
        # There's no search bar on SauceDemo, so we just simulate a search
        # by checking visible product names
        pass

    def get_displayed_product_names(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [elem.text for elem in elements]
