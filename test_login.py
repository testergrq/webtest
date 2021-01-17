import unittest
import pytest
from selenium import webdriver
from pages.login import LoginPage
from pages.index import IndexPage
from ddt import ddt,data
from datas import login

# @pytest.mark.all
class TestLogin():
    # @classmethod
    # def setUpClass(cls):
    #     pass
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    # def setUp(self):
    #     pass
    # def tearDown(self):
    #     pass
    # @pytest.mark.usefixtures('init_driver')
    # @pytest.mark.login
    # def test_login_1_success(self, init_driver):
    #     driver, login_page = init_driver
    #     login_page.clear_phone()
    #     login_page.clear_pwd()
    #     login_page.submit_userinfo(login.user_corrent['phone'], login.user_corrent['password'])
    #     user_ele = IndexPage(driver).get_user()
    #     assert ('python' in user_ele.text)

    @pytest.mark.usefixtures('my_setup_class')
    # @pytest.mark.usefixtures('init_driver')
    @pytest.mark.login
    @pytest.mark.parametrize('data',login.user_incorrent)
    # @data(*login.user_incorrent)
    def test_login_2_wrong(self,data,my_setup_class):
        driver,login_page=my_setup_class
        login_page.clear_phone()
        login_page.clear_pwd()
        login_page.submit_userinfo(data['phone'],data['password'])
        assert (data['expected']==login_page.alert_info().text)

    # @data(*login.user_unauthorized)
    # def test_login_3_unauthorized(self,data):
    #     self.login_page.submit_userinfo(data["phone"], data["password"])
    #     self.assertTrue(data["expected"] == self.login_page.unauthorized_info().text)


if __name__ == '__main__':
    unittest.main()