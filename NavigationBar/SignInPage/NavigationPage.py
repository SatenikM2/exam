from selenium.webdriver.common.by import By
from Base.BasePage import BasePage


class NavigationBarLocator():
    SearchFieldELemenetLocator = (By.ID, "searchAll")
    searchButtonlOcator = (By.XPATH, "//button[@type='submit']")
    homePageLocator = (By.XPATH, "//img[@alt='6pm - Your Premier Destination for Discount Fashion']")


class NavigationBar(NavigationBarLocator, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_search_field(self, text):
        searchFieldElement = self.driver.find_element(*(self.SearchFieldELemenetLocator))
        searchFieldElement.clear()
        searchFieldElement.send_keys(text)


    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(*(self.searchButtonlOcator))
        searchButtonElement.click()


    def go_to_home_page(self):
        homePage = self.driver.find_element(*(self.homePageLocator))
        homePage.click()

