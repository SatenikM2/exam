from selenium.webdriver.common.by import By
from Base.BasePage import BasePage



class ProductDetailsLocator():
    addToCartLocator = (By.XPATH, "//button[@data-track-value='Add-To-Cart']")


class ProductDetailsPage(ProductDetailsLocator, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_to_cart(self):
        productadd = self.driver.find_element(*(self.addToCartLocator))
        productadd.click()