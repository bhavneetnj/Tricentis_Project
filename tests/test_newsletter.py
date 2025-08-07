from pages.home_page import HomePage
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_newsletter_subscription(driver):
    home = HomePage(driver)
    email = f"subscriber{random.randint(1000,9999)}@testmail.com"

    home.subscribe_newsletter(email)
    message = home.get_newsletter_message()

    print(f"Newsletter message: '{message}'")

    assert "Thank you for signing up" in message or "already subscribed" in message
