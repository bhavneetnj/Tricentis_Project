from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    books_menu = (By.LINK_TEXT, "Books")
    search_input = (By.ID, "small-searchterms")
    search_button = (By.CSS_SELECTOR, "input.button-1.search-box-button")
    cart_quantity = (By.CSS_SELECTOR, "span.cart-qty")
    register_link = (By.LINK_TEXT, "Register")
    newsletter_email_input = (By.ID, "newsletter-email")
    newsletter_submit_button = (By.ID, "newsletter-subscribe-button")
    newsletter_result_message = (By.ID, "newsletter-result-block")

    def go_to_books(self):
        self.click(self.books_menu)

    def search_product(self, keyword):
        self.enter_text(self.search_input, keyword)
        self.click(self.search_button)

    def get_cart_count(self):
        return self.get_text(self.cart_quantity)

    def go_to_register(self):
        self.click(self.register_link)

    def subscribe_newsletter(self, email):
        # Wait for the email input to be visible before interacting
        newsletter_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.newsletter_email_input)
        )
        newsletter_input.clear()
        newsletter_input.send_keys(email)

        # Wait for the submit button and click
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.newsletter_submit_button)
        ).click()

    def get_newsletter_message(self):
        # Wait for the result message to be visible and return its text
        WebDriverWait(self.driver, 10).until(
             lambda driver: driver.find_element(*self.newsletter_result_message).text.strip() != ""
        )
        return self.driver.find_element(*self.newsletter_result_message).text