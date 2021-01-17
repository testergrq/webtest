import pytest

if __name__ == '__main__':
    pytest.main(['--clean-allure',
                '-m login',
                '--capture=no',
                 '--alluredir=allure'])
