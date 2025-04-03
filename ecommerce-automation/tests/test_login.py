from selenium import webdriver
from pages.login_page import LoginPage
import time


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")

    login_page = LoginPage(driver)
    login_page.open_login_modal()
    time.sleep(2)
    login_page.login("testuser5454", "testpass")
    time.sleep(3)

    assert "Welcome testuser" in driver.page_source
    driver.quit()


test_login()
