import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage

class LoginPage(BasePage):
    phone_input_locator=(By.NAME,'phone')
    pwd_input_locator=(By.NAME,'password')
    alert_locator=(By.XPATH,"//div[@class='form-error-info']")
    unathuorized_locator=(By.XPATH,"//div[@class='layui-layer-content']")
    get_user_locator=(By.XPATH,"//img[@class='mr-5']//..")
    def submit_userinfo(self,phone, pwd):
        phone_ele = self.get_visible_element(self.phone_input_locator)
        pwd_ele = self.get_visible_element(self.pwd_input_locator)
        phone_ele.send_keys(phone)
        pwd_ele.send_keys(pwd)
        phone_ele.submit()
        # time.sleep(3)
    def alert_info(self):
        return self.get_visible_element(self.alert_locator)
    def unauthorized_info(self):
        return self.get_visible_element(self.unathuorized_locator)

    def clear_phone(self):
        return self.get_phone_element().clear()
    def clear_pwd(self):
        return self.get_pwd_element().clear()
    def get_phone_element(self):
        return self.get_visible_element(self.phone_input_locator)
    def get_pwd_element(self):
        return self.get_visible_element(self.pwd_input_locator)