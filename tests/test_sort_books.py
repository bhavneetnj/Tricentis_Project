from pages.home_page import HomePage
from pages.book_page import BooksPage

def test_sort_books_low_to_high(driver):
    home = HomePage(driver)
    books = BooksPage(driver)

    home.go_to_books()
    books.sort_books_low_to_high()
    
    # Get prices (handling discounted prices)
    prices_elements = books.driver.find_elements(*books.product_prices)

    prices = [
        float(price.text.replace("$", "").replace("₹", "").split("\n")[-1].strip())
        for price in prices_elements
    ]

    print(f"Prices found: {prices}")

    assert prices == sorted(prices), "Books are not sorted by price (Low to High)"
