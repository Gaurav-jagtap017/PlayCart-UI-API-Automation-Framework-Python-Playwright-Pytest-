from .base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.get_by_label("Email Address")
        self.password_input = page.get_by_label("Password")
        self.login_btn = page.get_by_role("button", name="Login")

    def login(self, email, password):
        self.type(self.email_input, email)
        self.type(self.password_input, password)
        self.click(self.login_btn)
        self.wait_for_page_load()
