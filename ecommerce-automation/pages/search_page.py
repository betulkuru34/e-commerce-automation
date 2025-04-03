from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.laptops_category = (By.XPATH, "//a[@onclick=\"byCat('notebook')\"]")
        self.product_items = (By.CLASS_NAME, "card-title")  # Ürün başlıkları için bir sınıf adı

    def select_laptops_category(self):
        # Laptops kategorisine tıklayın
        laptops = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.laptops_category)
        )
        laptops.click()

    def verify_laptops_listed(self):
        # Ürünlerin listelendiğini doğrulayın
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.product_items)
        )
        return len(products) > 0
