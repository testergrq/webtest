from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging
from selenium.webdriver import Chrome
import time
logging.basicConfig(filename='test.log')
logger=logging.getLogger()

class BasePage:
    def __init__(self,driver:Chrome):
        self.driver=driver
    def get_visible_element(self,locator,eqc=20):
        try:
            return WebDriverWait(self.driver,eqc).until(
            ec.visibility_of_element_located(locator))
        except Exception as e:
            logger.error('no this element:{}'.format(e))
            self.driver.save_screenshot('log/{}.jpg'.format(time.time()))
            
    def switch_window(self,name=None,fqc=20):
        if name is None:
            current_handle=self.driver.current_window_handle
            WebDriverWait(self.driver,fqc).until(
                ec.new_window_is_opened(current_handle))
            handles=self.driver.window_handles
            return self.driver.switch_to.window(handles[-1])
        return self.driver.switch_to.window(name)