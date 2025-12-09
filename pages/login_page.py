from .base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.locator("//input[@data-qa='login-email']")
        self.password_input = page.get_by_placeholder("Password")
        self.login_btn = page.locator("//button[@data-qa='login-button']")
        self.error_message= page.get_by_text("Your email or password is incorrect!")

    def login(self, email, password):
        self.type(self.email_input, email)
        self.type(self.password_input, password)
        self.click(self.login_btn)
