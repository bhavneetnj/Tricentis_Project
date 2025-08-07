from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    product_titles = (By.CSS_SELECTOR, ".product-title a")

    def get_first_search_result_title(self):
        return self.get_text(self.product_titles)