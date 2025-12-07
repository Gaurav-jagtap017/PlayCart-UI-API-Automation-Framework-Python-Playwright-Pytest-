from playwright.sync_api import Page, expect
from .base_page import BasePage
import uuid
import random

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.latest_time = uuid.uuid4().hex[:4]

        # Page-1
        self.username = self.page.get_by_placeholder("Name")
        self.signup_email = self.page.locator("//input[@data-qa='signup-email']")
        self.signup_button = self.page.locator("//button[@data-qa='signup-button']")
        self.username_text= f"abcd{self.latest_time}"
        self.email_text= f"abcd{self.latest_time}@test.com"

        # Page-2
        self.account_info = self.page.get_by_text("Enter Account Information")
        self.address_info = self.page.get_by_text("Address Information")
        #Account Information
        self.mr_radio_button = self.page.locator("#id_gender1")
        self.password = self.page.get_by_label("Password ")
        self.days_dropdown = self.page.locator("#days")
        self.months_dropdown = self.page.locator("#months")
        self.years_dropdown = self.page.locator("#years")
        #Address Information
        self.first_name = self.page.get_by_label("First name ") 
        self.last_name = self.page.get_by_label("Last name ")
        self.company_name = self.page.locator("#company")
        self.address1 = self.page.locator("#address1")
        self.address2 = self.page.locator("#address2")
        self.country_dropdown = self.page.get_by_label("Country")
        self.state = self.page.get_by_label("State ")
        self.city = self.page.get_by_label("City ")
        self.zipcode = self.page.locator("#zipcode")
        self.mobile_number = self.page.get_by_label("Mobile Number ")
        self.create_button = self.page.get_by_role("button", name="Create Account")

    def goto_register_page(self):
        self.username.fill(self.username_text)
        self.signup_email.fill(self.email_text)
        self.signup_button.click()

        self.page.wait_for_url("**/signup")
        expect(self.account_info).to_be_visible()
        expect(self.address_info).to_be_visible()

        # return same instance instead of creating a new one
        return self

    def enter_details_and_create_user(self):
        self.mr_radio_button.click()
        self.password.fill("RandomPass@123")
        self.days_dropdown.select_option(str(random.randrange(1,32)))
        self.months_dropdown.select_option(str(random.choice(months)))
        self.years_dropdown.select_option(str(random.randrange(1900,2021)))

        self.first_name.fill(f"abcdsdfdfh")
        self.page.wait_for_timeout(0.2)
        self.last_name.fill(f"xyzefg")
        self.company_name.fill("companyxy")
        self.address1.fill("Street 15, P.O. box, companyxy, phase1")
        self.address2.fill("City name")
        #self.country_dropdown.select_text("India")
        self.state.fill("Mahanrastra")
        self.city.fill("PuneCity")
        self.page.wait_for_timeout(0.2)
        self.zipcode.fill(str(random.randint(100000, 999999)))
        self.mobile_number.fill(str(random.randint(7600000000,9900000000)))
        self.create_button.click()
