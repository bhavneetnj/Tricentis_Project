# Tricentis Demo Web Shop Automation Framework

This project contains an automated test framework for the [Tricentis Demo Web Shop](https://demowebshop.tricentis.com) using **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** design pattern.

## 🚀 Project Overview

The goal of this framework is to automate and validate key functionalities of the Tricentis demo webshop, such as:

- User Registration
- Product Search
- Adding/Removing items from the Cart
- Sorting products in the Books section
- Newsletter Subscription

## 📂 Project Structure

tricentis_webshop_automation/
│
├── pages/ # Page Object Model classes
│ ├── base_page.py
│ ├── home_page.py
│ ├── register_page.py
│ ├── books_page.py
│ ├── search_page.py
│ └── cart_page.py
│
├── tests/ # Pytest test scripts
│ ├── test_registration.py
│ ├── test_search.py
│ ├── test_cart.py
│ ├── test_books_sorting.py
│ └── test_newsletter.py
│
├── test_data/ # Test data files
│ └── users.json
│
├── conftest.py # Fixtures and configuration
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🧪 Test Scenarios

1. **User Registration**
   - Register new user with unique credentials
   - Validate successful registration message

2. **Product Search**
   - Search for existing product keywords
   - Verify search results match the keyword

3. **Cart Operations**
   - Add and remove items to/from the shopping cart
   - Validate cart count and subtotal

4. **Books Sorting**
   - Sort books by price (Low to High, High to Low)
   - Verify sorting functionality

5. **Newsletter Subscription**
   - Subscribe to the newsletter with a valid email
   - Validate subscription success message

## 🛠️ Tools & Technologies

- Python 3.x
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- JSON/CSV for test data
- ChromeDriver / WebDriver Manager

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/tricentis-webshop-automation.git
   cd tricentis-webshop-automation
