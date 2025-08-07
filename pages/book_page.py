from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BooksPage(BasePage):
    first_add_to_cart_button = (By.CSS_SELECTOR, ".product-item .product-box-add-to-cart-button")
    sort_dropdown = (By.ID, "products-orderby")
    product_prices = (By.CSS_SELECTOR, ".product-item .prices")

    def add_first_book_to_cart(self):
        self.click(self.first_add_to_cart_button)

    def sort_books_low_to_high(self):
        self.select_dropdown_by_text(self.sort_dropdown, "Price: Low to High")

    def get_book_prices(self):
        prices = self.driver.find_elements(*self.product_prices)
        return [float(p.text.replace("$", "").replace("₹", "").strip()) for p in prices]
