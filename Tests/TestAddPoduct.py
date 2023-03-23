import time

from selenium import webdriver
import unittest
from NavigationBar.SignInPage import SignInPage
from ProductPage.SearchField import SearchResultPage
from ProductPage.ProductDetailPage import ProductDetailsPage
from NavigationBar.SignInPage.NavigationPage import NavigationBar
from NavigationBar.SignInPage.CartPage import Cart

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.6pm.com/")
        time.sleep(5)
        self.navigationBarObj = NavigationBar(self.driver)
        self.searchResultObj = SearchResultPage(self.driver)
        self.productDetailsObj = ProductDetailsPage(self.driver)
        self.cartObject = Cart(self.driver)



    def test_signIn(self):
        self.navigationBarObj.fill_search_field("adidas ultraboots")
        time.sleep(3)
        self.navigationBarObj.click_to_search_button()
        time.sleep(3)
        self.cartObject.choose_for_men()
        time.sleep(3)
        self.cartObject.click_first_product()
        time.sleep(5)
        self.cartObject.choose_product_size()
        time.sleep(5)
        self.productDetailsObj.add_to_cart()
        time.sleep(3)
        # self.navigationBarObj.go_to_home_page()





    def tearDown(self) -> None:
        self.driver.close()