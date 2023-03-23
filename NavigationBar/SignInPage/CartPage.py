from Base.BasePage  import BasePage
from NavigationBar.SignInPage.NavigationPage import NavigationBar
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartLocator():
    chooseForMenLocator = (By.XPATH, "//ul[@aria-labelledby='txAttrFacet_Gender']/li[2]")
    firstProductLocator = (By.XPATH, "//a[@data-style-id='5811252']")
    productSizeLocator = (By.XPATH, "//label[@for='radio-2827-9593349']")



class Cart(CartLocator, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navBarObject = NavigationBar(self.driver)


    def choose_for_men(self):
        delFirstProduct = self.driver.find_element(*(self.chooseForMenLocator))
        delFirstProduct.click()


    def click_first_product(self):
        firstProduct = self.driver.find_element(*(self.firstProductLocator))
        firstProduct.click()


    def choose_product_size(self):
        productSize = self.driver.find_element(*(self.productSizeLocator))
        productSize.click()






