from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class CartPage:
    def __init__(self, driver):
        self.driver = driver

        # Ürün başlığına tıklanacak (tüm ürün başlıkları hrefch class'ında)
        self.product_link_xpath = (By.XPATH, "//a[@class='hrefch']")

        # "Add to cart" butonu
        self.add_to_cart_button = (By.XPATH, "//a[contains(text(),'Add to cart')]")

        # Sepet bağlantısı
        self.cart_link = (By.ID, "cartur")

        # Sepet içeriği
        self.cart_items = (By.CLASS_NAME, "table-responsive")

    def select_product(self):
        """Ürün listesinden ilk ürünü seçer ve tıklar."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "tbodyid"))
        )

        for attempt in range(3):
            try:
                product = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.product_link_xpath)
                )
                product.click()
                break
            except StaleElementReferenceException:
                print(f"[UYARI] StaleElementReferenceException yakalandı, tekrar deneme: {attempt + 1}")
                continue

    def add_product_to_cart(self):
        """Seçilen ürün sayfasında 'Add to cart' butonuna tıklar ve alert'i kapatır."""
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_button.click()

        # Alert kutusu beklenip onaylanır
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print("ALERT MESAJI:", alert.text)
        alert.accept()

    def open_cart(self):
        """Sayfanın üst kısmındaki 'Cart' bağlantısına tıklar."""
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)
        )
        cart_link.click()

    def verify_cart(self):
        """Sepette ürün olup olmadığını kontrol eder."""
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.cart_items)
        )
        return len(items) > 0

    def get_product_name_from_detail_page(self):
        """
        Ürün detay sayfasındaki başlığı döner.
        """
        product_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "name"))
        )
        return product_name.text.strip()

    def get_product_name_from_cart(self):
        """
        Sepet sayfasındaki ilk ürünün adını döner.
        """
        product_name_in_cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr/td[2]"))  # 2. hücre: ürün adı
        )
        return product_name_in_cart.text.strip()
