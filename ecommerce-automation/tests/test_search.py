from selenium import webdriver
from pages.search_page import SearchPage


def test_laptops_category():
    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")

    search_page = SearchPage(driver)

    # Laptops kategorisini seç
    search_page.select_laptops_category()

    # Laptops kategorisindeki ürünleri doğrula
    assert search_page.verify_laptops_listed(), "Laptops kategorisinde ürün bulunamadı!"

    driver.quit()
test_laptops_category()