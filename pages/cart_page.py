from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    cart_label_link = (By.CLASS_NAME, "cart-label")
    cart_item_names = (By.CSS_SELECTOR, ".cart .product-name")

    def go_to_cart(self):
        self.click(self.cart_label_link)

    def get_cart_items(self):
        items = self.driver.find_elements(*self.cart_item_names)
        return [item.text for item in items]