from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.BasePage import BasePage
import time


class SerachResultPageLocator():
    firstProductLocator = (By.XPATH, "((//img[@class='s-image'])[1])")


class SearchResultPage(SerachResultPageLocator, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_to_first_product(self):
        firstProductElement = self.driver.find_element(*(self.firstProductLocator))
        firstProductElement.click()

