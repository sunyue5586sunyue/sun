import os
import sys
sys.path.append(os.getcwd())
import pytest
from page.page_login import PageLogin


def get_data():
    return [("13811110000", "123456"), ("13811110001", "1234")]


class TestLogin(object):
    def setup_class(self):
        self.login = PageLogin()

    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("phone, pwd", get_data())
    def test_login(self, phone, pwd):
        self.login.page_login(phone, pwd)
