import page
from base.base import Base


class PageLogin(Base):
    def page_input_phone(self, phone):
        self.base_input(page.login_phone, phone)

    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    def page_click_but(self):
        self.base_click(page.login_btn)

    def page_login(self, phone, pwd):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_but()
