import unittest
from selenium import webdriver
from pages.login import LoginPage
from pages.index import IndexPage
from pages.bid import BidPage
from datas import login,bid
from ddt import ddt,data
import pytest
#登录、有余额、有标、标有余额
#1、手动
# 2、自动化ui
# 3、接口
# @ddt
class TestBid():
    # @classmethod
    # def setUpClass(cls):
    #     pass
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://120.78.128.25:8765/Index/login.html")
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.submit_userinfo(
    #         login.user_corrent['phone'],login.user_corrent['password'])
    #     self.bid_page=BidPage(self.driver)
    #
    # def tearDown(self):
    #     self.driver.quit()
    @pytest.mark.usefixtures('bid_init_driver')
    @pytest.mark.bid
    def test_bid_success(self,bid_init_driver):
        driver, login_page,bid_page = bid_init_driver
        #首页点击投标
        IndexPage(driver).bid()
        # 投标页面输入投标
        # data_amout=self.bid_page.data_amout()
        # print(type(data_amout))
        bid_page.bid(bid.bid_correct['money'])
        bid_page.click_bid_submit()
        #断言
        assert (bid_page.popup_text()==bid.bid_correct['expected'])
        #比对金额
        assert (int(bid_page.data_amout)-100.00==int(bid_page.data_amout))
        #投资记录
if __name__ == '__main__':
    unittest.main()
    ele=driver.find_element()
