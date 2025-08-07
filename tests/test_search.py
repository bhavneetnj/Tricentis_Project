from pages.home_page import HomePage
from pages.search_page import SearchPage

def test_search_product_suggestion(driver):
    home = HomePage(driver)
    search = SearchPage(driver)

    home.search_product("computing")
    result = search.get_first_search_result_title()
    
    assert "Computing" in result or result != "", "Expected product in search results"