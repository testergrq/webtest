from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage
from pages.login import LoginPage

class IndexPage(BasePage):#首页
    bid_ele_locator=(By.XPATH,"//a[contains(@class,'btn-special')]")
    def get_user(self):
        return self.get_visible_element(LoginPage.get_user_locator)
    def bid(self):
        return self.get_bid_button().click()
    def get_bid_button(self):
        return self.get_visible_element(self.bid_ele_locator)
