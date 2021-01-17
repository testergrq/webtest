import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage

class BidPage(BasePage):
    bid_input_locator=(By.XPATH,"//input[contains(@class,'invest-unit-invest')]")
    #用来断言
    bid_popup_locator=(By.XPATH,
        "//div[contains(@class,'layui-layer-content')]//div[contains(@class,'capital_font1')]")
    bid_submit_locator=(By.XPATH,"//button[contains(@class,'btn btn-special height_style')]")
    def bid(self,money):
        return self.bid_input.send_keys(money)
    @property
    def bid_input(self):
        return self.get_visible_element(self.bid_input_locator)

    @property
    def bid_submit(self):
        return self.get_visible_element(self.bid_submit_locator)

    @property
    def bid_popup(self):
        return self.get_visible_element(self.bid_popup_locator)
    def click_bid_submit(self):
        return self.bid_submit.click()
    def popup_text(self):
        return self.bid_popup.text
    @property
    def data_amout(self):
        return self.bid_input.get_attribute('data-amount')
