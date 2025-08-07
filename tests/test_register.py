from pages.home_page import HomePage
from pages.register_page import RegisterPage
import time
import random

def test_register_user(driver):
    home = HomePage(driver)
    register = RegisterPage(driver)

    home.go_to_register()
    email = f"testuser{random.randint(1000,9999)}@example.com"
    register.fill_registration_form("Test", "User", email, "Test@1234")
    message = register.get_success_message()
    
    assert "Your registration completed" in message