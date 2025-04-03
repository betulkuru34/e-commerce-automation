from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.place_order_button = (By.XPATH, "//button[text()='Place Order']")
        self.modal = (By.ID, "orderModal")
        self.name_field = (By.ID, "name")
        self.country_field = (By.ID, "country")
        self.city_field = (By.ID, "city")
        self.card_field = (By.ID, "card")
        self.month_field = (By.ID, "month")
        self.year_field = (By.ID, "year")
        self.purchase_button = (By.XPATH, "//button[text()='Purchase']")
        self.confirmation_message = (By.CLASS_NAME, "sweet-alert")

    def place_order(self):
        # Sipariş ver butonuna tıkla
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.place_order_button)
        )
        place_order_button.click()
        # Modal penceresini bekle
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.modal)
        )

    def fill_payment_details(self, name, country, city, card, month, year):
        # Ödeme bilgilerini doldur
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.name_field)
        ).send_keys(name)
        self.driver.find_element(*self.country_field).send_keys(country)
        self.driver.find_element(*self.city_field).send_keys(city)
        self.driver.find_element(*self.card_field).send_keys(card)
        self.driver.find_element(*self.month_field).send_keys(month)
        self.driver.find_element(*self.year_field).send_keys(year)

    def complete_purchase(self):
        # Satın alma işlemini tamamla
        purchase_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.purchase_button)
        )
        purchase_button.click()

    def verify_confirmation_message(self):
        # Onay mesajını doğrula
        confirmation = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.confirmation_message)
        )
        return "Thank you for your purchase!" in confirmation.text
