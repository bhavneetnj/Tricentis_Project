from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    gender_male_radio = (By.ID, "gender-male")
    first_name_input = (By.ID, "FirstName")
    last_name_input = (By.ID, "LastName")
    email_input = (By.ID, "Email")
    password_input = (By.ID, "Password")
    confirm_password_input = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")
    success_message = (By.CLASS_NAME, "result")

    def fill_registration_form(self, first_name, last_name, email, password):
        self.click(self.gender_male_radio)
        self.enter_text(self.first_name_input, first_name)
        self.enter_text(self.last_name_input, last_name)
        self.enter_text(self.email_input, email)
        self.enter_text(self.password_input, password)
        self.enter_text(self.confirm_password_input, password)
        self.click(self.register_button)

    def get_success_message(self):
        return self.get_text(self.success_message)