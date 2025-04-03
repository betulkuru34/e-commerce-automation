from selenium import webdriver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_empty_cart():
    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")

    cart_page = CartPage(driver)
    cart_page.open_cart()

    # Ödeme işlemini başlat
    checkout_page = CheckoutPage(driver)
    try:
        checkout_page.place_order()
    except Exception as e:
        assert "No items in the cart" in str(e), "Beklenen hata mesajı alınamadı!"

    driver.quit()
test_checkout_empty_cart()
