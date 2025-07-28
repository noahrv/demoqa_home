from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com'

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def visit(self):
        return self.driver.get(self.base_url)

    def get_text(self):
        return str(self.find_element().text)
