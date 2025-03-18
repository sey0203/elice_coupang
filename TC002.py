from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


# TC001 장바구니 담기 기능 테스트


class ProductPage:
    ITEM_XPATH = "//form//ul/li[1]//a"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_first_item(self):
        wait = ws(self.driver, 10)
        first_item = wait.until(EC.element_to_be_clickable((By.XPATH, self.ITEM_XPATH)))
        first_item.click()


class Add_Cart:
    CART_BUTTON_XPATH = "//button[contains(text()='장바구니 담기')]"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_to_cart(self):
        wait = ws(self.driver, 10)
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON_XPATH)))
        cart_button.click()