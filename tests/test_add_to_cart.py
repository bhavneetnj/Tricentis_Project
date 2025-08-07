from pages.home_page import HomePage
from pages.book_page import BooksPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_add_book_to_cart(driver):
    home = HomePage(driver)
    books = BooksPage(driver)
    cart = CartPage(driver)

    home.go_to_books()
    assert "books" in driver.current_url.lower()

    books.add_first_book_to_cart()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.cart-qty"), "(1)"
    )
)   
    
    cart_count = home.get_cart_count().strip("()")
    assert cart_count == "1", f"Cart count should be 1 after adding book, but was {cart_count}"