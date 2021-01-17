import pytest
from selenium import webdriver
from pages.login import LoginPage
from pages.bid import BidPage
from datas import login,bid
import win32gui
import win32con

@pytest.fixture
def init_driver():
    print('begin driver')
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    driver.get('http://120.78.128.25:8765/Index/login.html')
    yield (driver,login_page)#相当于setup
    #生成器，迭代器
    driver.quit()
    print('quit driver')

@pytest.fixture(scope='class')
def my_setup_class():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    driver.get('http://120.78.128.25:8765/Index/login.html')
    yield (driver, login_page)  # 相当于setupclass
    # 生成器，迭代器
    # driver.quit()

@pytest.fixture()
def bid_init_driver():
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    login_page = LoginPage(driver)
    login_page.submit_userinfo(
        login.user_corrent['phone'], login.user_corrent['password'])
    bid_page = BidPage(driver)
    yield (driver,login_page,bid_page)#相当于setup
    #生成器，迭代器
    driver.quit()
