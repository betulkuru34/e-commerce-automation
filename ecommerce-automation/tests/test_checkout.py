from selenium import webdriver
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_success():
    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")

    # Ürün kategorisine git ve bir ürün seç
    search_page = SearchPage(driver)
    search_page.select_laptops_category()
    cart_page = CartPage(driver)
    cart_page.select_product()
    cart_page.add_product_to_cart()
    cart_page.open_cart()

    # Ödeme işlemini başlat
    checkout_page = CheckoutPage(driver)
    checkout_page.place_order()
    checkout_page.fill_payment_details(
        name="Betül Kuru",
        country="Turkey",
        city="Ankara",
        card="1234567890123456",
        month="12",
        year="2025"
    )
    checkout_page.complete_purchase()

    # Satın alma onayını doğrula
    assert checkout_page.verify_confirmation_message(), "Satın alma başarısız!"
    driver.quit()
test_checkout_success()
