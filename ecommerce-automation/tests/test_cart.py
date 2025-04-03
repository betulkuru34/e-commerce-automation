from selenium import webdriver
from pages.search_page import SearchPage
from pages.cart_page import CartPage


def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")

    cart_page = CartPage(driver)

    cart_page.select_product()
    expected_product_name = cart_page.get_product_name_from_detail_page()

    cart_page.add_product_to_cart()
    cart_page.open_cart()

    actual_product_name = cart_page.get_product_name_from_cart()

    assert expected_product_name == actual_product_name, \
        f"Ürün uyuşmazlığı: Beklenen '{expected_product_name}', fakat sepette '{actual_product_name}' bulundu."

    driver.quit()

test_add_to_cart()